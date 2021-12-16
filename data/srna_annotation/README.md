#srna annotation

I first downloaded the e. coli K12 genome (Juun 16, 2021) from NCBI. Then I extracted all
ncRNAS and antisense_rna entries from the fasta using the gff annotation.
Then I just blasted all of the sRNAs from K12 to the UPEC (536) genome and took for each
query only the match with the lowest p-value, using :

```bash
blastn -query srnas.fasta -subject ecoli536.fasta -max_target_seqs 1 -out blast_srnas.txt -outfmt 6
```

Then I manually assembled additional gff lines to put the sRNA annotations to the gff file.

```bash
awk '{if ($9<$10) {print "CP000247.1\tGenbank\tsRNA\t" $9 "\t" $10 "\t.\t+\t.\tID=" $1 ";gene=" $1 ";locus_tag=" $1;} else print "CP000247.1\tGenbank\tsRNA\t" $10 "\t" $9 "\t.\t-\t.\tID=" $1 ";gene=" $1 ";locus_tag=" $1}' blast_srnas.txt >> ../reference_sequences/ecoli536_sRNAs.gff3 
```

