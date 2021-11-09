"""
Here we create gff and fasta file with only start regions to search for off-targets. We use seqmap to identify them.
"""

import re
import json
import subprocess
from Bio import SeqIO
import os
from Bio.SeqUtils import GC
import pandas as pd
from Bio.Seq import Seq

# first, we generate target sequences from the PNA sequences for the off-target algorithm:
with open("../data/off_targets_search/pnas.fasta") as pna:
    with open("../data/off_targets_search/pnas_targets.fasta", "w") as targets:
        for record in SeqIO.parse(pna, "fasta"):
            print(record.name)
            print(record.seq.reverse_complement())
            print(record)
            record.seq = record.seq.reverse_complement()
            print(record.seq[::-1])
            SeqIO.write(record, targets, "fasta")
            record.seq = record.seq[::-1]
            record.description = record.description + " reverse"
            SeqIO.write(record, targets, "fasta")


# create new gff with only ess. genes:
length_region = 20

# create gff with only starts of genes:
with open("../data/reference_sequences/ecoli536_sRNAs.gff3") as origin_file:
    f_start_regions = open("../data/off_targets_search/start_regions.gff", "w")

    headers = re.compile(r"##")
    mRNA = re.compile(r"\tCDS\t|\trRNA\t|\ttRNA\t|\tsRNA\t")

    for line in origin_file:
        if headers.match(line):
            f_start_regions.write(line)
        # write new start_region_gffs one for nonessential genes and one for all genes:
        elif mRNA.search(line):
            line = line.split("\t")
            s = int(line[3])
            e = int(line[4])
            # from-30 to + 15 from start!
            if line[6] == "+":
                line[3] = str(s - 30)
                line[4] = str(s + 15)
            else:
                line[3] = str(e - 15)
                line[4] = str(e + 30)
            f_start_regions.write("\t".join(line))
    f_start_regions.close()

# create gff withOUT starts of genes:
with open("../data/reference_sequences/ecoli536_sRNAs.gff3") as origin_file:
    f_start_regions = open("../data/off_targets_search/without_start_regions.gff", "w")

    headers = re.compile(r"##")
    mRNA = re.compile(r"\tCDS\t|\trRNA\t|\ttRNA\t|\tsRNA\t")

    for line in origin_file:
        if headers.match(line):
            f_start_regions.write(line)
        # write new start_region_gffs one for nonessential genes and one for all genes:
        elif mRNA.search(line):
            line = line.split("\t")
            s = int(line[3])
            e = int(line[4])
            # from-30 to + 15 from start!
            if line[6] == "+":
                line[3] = str(s + 15)
                line[4] = str(e)
            else:
                line[3] = str(s)
                line[4] = str(e - 15)
            f_start_regions.write("\t".join(line))
    f_start_regions.close()

# generate fasta of all gene start regions:
subprocess.call(["gffread", "-w", "../data/off_targets_search/start_regions1.fa", "-g",
                 "../data/reference_sequences/ecoli536.fasta",
                 "../data/off_targets_search/start_regions.gff", "-F"])
# generate fasta of all genes without start regions:
subprocess.call(["gffread", "-w", "../data/off_targets_search/without_start_regions1.fa", "-g",
                 "../data/reference_sequences/ecoli536.fasta",
                 "../data/off_targets_search/without_start_regions.gff", "-F"])

# now change the fasta to locus tags headers:
subprocess.call("(sed -E 's/gene-([^ ]+).*/\\1/' ../data/off_targets_search/start_regions1.fa | "
                " sed -E 's/.*locus_tag=([^ ]+).*/>\\1/' > "
                "../data/off_targets_search/start_regions.fa)", shell=True)

subprocess.call("(sed -E 's/gene-([^ ]+).*/\\1/' ../data/off_targets_search/without_start_regions1.fa | "
                " sed -E 's/.*locus_tag=([^ ]+).*/>\\1/' > "
                "../data/off_targets_search/without_start_regions.fa)", shell=True)


# delete unmodified file:
os.remove("../data/off_targets_search/start_regions1.fa")
os.remove("../data/off_targets_search/without_start_regions1.fa")

# now I manually assembled all pna target sequences using:
# my_pna = Seq("CTCATCTGTC")
# print(my_pna.reverse_complement())
# for each PNA to get the target sequence. it is saved as "pna_targets.fasta"

# now I check off-targets with up to 2 mm in target regions ....
# (I ran it in terminal, because subprocess didnt work somehow...)
subprocess.call(
    ["seqmap", "2", "../data/off_targets_search/pna_targets.fasta",
     "../data/off_targets_search/start_regions.fa",
     "../data/off_targets_search/pna_2mm_startregions.tab", "/output_all_matches", "/available_memory:200",
     "/forward_strand"],
    shell=True)
subprocess.call(
    ["seqmap", "2", "../data/off_targets_search/pna_targets.fasta",
     "../data/off_targets_search/without_start_regions.fa",
     "../data/off_targets_search/pna_2mm_otherregions.tab", "/output_all_matches", "/available_memory:200",
     "/forward_strand"],
    shell=True)


# ... and in the whole ehec genome
subprocess.run(
    ["seqmap", "2", "../data/off_targets_search/pna_targets.fasta",
     "../data/reference_sequences/ecoli536.fasta",
     "../data/off_targets_search/pna_2mm_wholegenome.tab", "/output_all_matches", "/available_memory:200"],
    shell=True)













