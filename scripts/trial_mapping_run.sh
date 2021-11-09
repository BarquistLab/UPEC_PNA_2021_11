#!/bin/bash


PROJECT=../data
NAME=../data/fastq/L2100396_1_w_o_control.fq.gz

mkdir -pv $PROJECT/libs
NEWNAME=${NAME##*/}
NEWNAME=${NEWNAME%.fastq.gz}_trimmed.fastq.gz

/bin/bbmap/bbduk.sh -Xmx1g in=$NAME ref=/bin/bbmap/resources/adapters.fa t=20 out=$PROJECT/libs/${NEWNAME}\
		     ktrim=r k=23 mink=11 hdist=1 qtrim=r trimq=10 #ftl=12

mkdir -pv $PROJECT/rna_align
DIR=$PROJECT/rna_align

/bin/bbmap/bbmap.sh in=$PROJECT/libs/${NEWNAME} trimreaddescription=t  t=20 ref=$PROJECT/reference_sequences/ecoli536.fasta\
		     k=8 ambig=random outm=$DIR/$NAME.sam

