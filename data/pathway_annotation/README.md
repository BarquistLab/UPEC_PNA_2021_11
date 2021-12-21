# Pathway annotation

Here are the files which I used for annotion of regulons  and pathways. 

### regulonDB.txt

date of download: 06-12-2021

downloaded tabular file of all regulons from *E. coli* K12. Link:  [https://regulondb.ccg.unam.mx/](https://regulondb.ccg.unam.mx/)

### codingseqs.gff

gff file with all CDS, generated using [../reference_sequences/ecoli536.gff](../reference_sequences/ecoli536.gff) and some simple bash commands.

### ecoli_cds.fasta

fasta file with all coding sequences, produced by codingseqs.gff and the reference fasta file [../reference_sequences/ecoli536.fasta](../reference_sequences/ecoli536.fasts) and the bedtools getfasta command.

### eggnogg_output.tsv/.xlsm

date of download: 05-05-2021

These eggnog output tabfiles were created on the eggnogg-mapper (v2) website [http://eggnog-mapper.embl.de/](http://eggnog-mapper.embl.de/), using the ecoli_cds file as an input and leaving all other measured in the standard settings. 