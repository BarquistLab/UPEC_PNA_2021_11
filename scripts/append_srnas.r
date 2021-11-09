library(dplyr)

setwd("~/Documents/pna_rnaseq_experiments/upec_transcriptomics_03_21/scripts")
srnas_raw <- read_delim("../data/reference_sequences/srnas.tsv", delim = "\t",col_names = F)

srnas <- srnas_raw %>% mutate(X9 = gsub("NC_\\d+_([^\\(]+).*", "\\1", X9))
srnas$X9 <- make.unique(srnas$X9)
srnas$X9 <- gsub("(.*)","ID=\\1;locus_tag=\\1", srnas$X9 )

write_delim(srnas, col_names = F, "../data/reference_sequences/srnas.tsv", delim = "\t")
