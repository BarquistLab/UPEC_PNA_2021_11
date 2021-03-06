#!/bin/bash
main(){
    # go to project directory where the reads and reference
    # sequences are stored:
    PROJECT=../data
    echo "Start trimming"
    rename_trim_rna_libs
    echo "Trimming done. Start maopping"
    align_rna_reads_genome
    echo "Finished mapping. Start connecting all tab files"
    featureCounts -T 5 -t CDS,sRNA -g locus_tag \
		  -a $PROJECT/reference_sequences/FQ312003.1.gff \
		  -o $PROJECT/rna_align/counttable.txt \
		  $PROJECT/rna_align/*.bam
}

rename_trim_rna_libs(){
    mkdir -pv $PROJECT/libs
    for NAME in $(ls $PROJECT/fastq/*.fastq.gz)
    do
        echo "$NAME starts trimming nowwwwwww"
        NEWNAME=${NAME##*/}
        NEWNAME=${NEWNAME%.fastq.gz}_trimmed.fastq.gz
        echo $NEWNAME
       # bbduk trims low quality bases and removes adapters:
        ~/bin/bbmap/bbduk.sh -Xmx1g in=$NAME \
			     ref=~/bin/bbmap/resources/adapters.fa t=20\
			     out=$PROJECT/libs/${NEWNAME} ktrim=r k=23 mink=11\
			     hdist=1 qtrim=r trimq=10
    done
}


align_rna_reads_genome(){
    mkdir -pv $PROJECT/rna_align
    DIR=$PROJECT/rna_align
    for i in $(ls $PROJECT/libs/*.fastq.gz)
    do
        NAME=${i##*/}
        NAME=${NAME%_trimmed.fastq.gz}
        echo "Starting mapping for sample: $NAME"
        ~/bin/bbmap/bbmap.sh in=$i trimreaddescription=t  t=20 \
			     ref=$PROJECT/reference_sequences/FQ312003_wplasmids.fa \
			     k=8 ambig=random outm=$DIR/$NAME.bam
        # sort sam file, create BAM file:
        samtools sort -O BAM -@ 40 $DIR/$NAME.sam > $DIR/$NAME
	samtools index $DIR/$NAME.bam                                                                                                                             
        # remove sam file: (not actually needed)                                                                                                                  
        rm $DIR/$NAME.sam                                                                                                                                         
    done                                                                                                                                                          
}                                                                                                                                                                 
                                                                                                                                                                  
main      
