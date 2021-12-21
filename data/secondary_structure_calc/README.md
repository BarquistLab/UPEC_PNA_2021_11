# Secondary structure prediction 

Here, we predict mRNA secondary structure of the mRNA around the start codon of PNA-targetrd genes. We think it might have an influence on PNA binding. 



## data import and preparation

First, we want to predict the secondary structure for all gene targets. To do this, we need to extract the regions around the start codons of each gene. We first select the target genes from our gff and change the locations to the start regions (- 50 bp from the start):

```bash
grep -E "ECP_3909|ECP_4268|ECP_0097|ECP_3157|ECP_0179|ECP_3906|ECP_0535|ECP_3905|ECP_4195|ECP_3394|ECP_2607|ECP_2656|ECP_1086|ECP_0027" ../reference_sequences/ecoli536_sRNAs.gff3 | \
grep -P "\tCDS\t" |  \
awk -F'\t' 'BEGIN { OFS="\t" } {if ($7=="-") {$5=$5+40; $4=$5-91} else { $4=$4-40; $5=$4+91} print $0}' > start_regions.gff3
```

Now we need to extract these start sequences from the fasta file to be able to run secondary structure predictions on it. We use gffread (v0.11.7) for that:

```bash
gffread start_regions.gff3 -g ../reference_sequences/ecoli536.fasta -x start_regions.fasta
```

Now we can predict the MFE of each of the mRNAs using RNAfold (v2.4.14) and create a tab file with structural data and predicted MFEs:

```bash
echo -e "gene\tmRNA_sequence\tbinding\tMFE" > sec_structure.tsv
```

```bash
RNAfold -i start_regions.fasta | perl -pe 's/\n/\t/g; s/>//; s/\s+/\t/; s/\(-|\( -/-/; s/\)\t$/\n/' | sed 's/gene-//' >> sec_structure.tsv 
```

Now we can use the data to check sec. structures and MFE.



All the .eps picture files are generated manually on the [RNAfold web server](http://rna.tbi.univie.ac.at/cgi-bin/RNAWebSuite/RNAfold.cgi) (20-12-2021). 

