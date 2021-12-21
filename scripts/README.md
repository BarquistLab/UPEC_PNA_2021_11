# scripts

Here, all scripts needed to produce the results and plots are stored.



### trimm_map_BB.sh

The script loops through the fastq-files, trims of adapters using BBDuk, maps against the reference UPEC genome (reference fasta and gff files can be found in [../data/reference_sequences/](../data/reference_sequences/)) and counts the reads mapped to coding sequences and sRNAs using featureCounts.

Trimming, mapping and counting statistics are stored in the log file [../analysis/logfile.log](../analysis/logfile.log) . The directory [../data/rna_align](../data/rna_align) includes all bam-alignment files as well as the count table [../data/rna_align/counttable.txt](../data/rna_align/counttable.txt) . This count will be imported into R for Differential expression analysis.

### ref

reference/indexes directory created by BBtools.



### PNA_RNASEQ_upec.Rmd

R markdown script to perform DE analysis, pathway enrichment analysis etc. 

### check_offtargets.py

python script to perform off-target search, used for volcanoplots.



