## beeswarm plots

- beeswarm_downregulated.svg : bs plot (the one as I did before, 1 mm pff-targets with their mismatch positions)
- beeswarm_upregulated.svg : the one you wanted (right?), with all upregulated 1 mm off-targets



## diff_exp_rawdata

different raw output DE files in csv format

## volcanoplots_bc

Volcanoplots from the DE data. volcanoes ending with _otherots.svg are off-targets that bind within the CDS (starting from 15 nucleobases inside the CDS to end)

## PCA_plots

PCA plots which I made with the new batcheffects removal technique, which worked actually better. 

- PCA_acpP_after_batcheffect_removal.svg : PCA of only acpP samples after batcheffect removal
- PCA_all_samples_A_before_B_after_batcheffect_removal.svg : two PCA plots, A is before batcheffect removal, b is after. 

## pathway_analysis

- kegg raw result files (in csv format)
- hm_KEGG.svg : pathway heatmap (as you wanted)

## mismatch_positions

csv files with the respective mismatch positions. files ending with _all_offtargets show all off-targets with 1 and 2 mismatches, while others just show the ones that are diff. downregulated.

## heatmaps

Different heatmaps:

- hm_0_Ot_de_new.svg : HM showing all 0 mismatch targets (and off-targets)
- hm_acpp_5_highest.svg : showing only 5 top upregulated / downregulated genes of acpP and scr samples
- hm_acpp_10_highest.svg : Same HM but with 10 top genes
- hm_all_genes_all_samples_clustering.svg : The new one you wanted which shows logCPM values for all genes with clustering of samples
- hm_high_de_new.svg : highest DE genes for the samples
- hm_srnas_new.svg : showing only sRNAs
- hm_targets_new.svg : showing only target genes with respective up/downregulations. 

