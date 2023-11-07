# VCF_context
Fetches functional annotation, AlphaMissense Prediction and generates structures for variants on a VCF file

#Step 1: Annotate VCF with Annovar
perl table_annovar.pl example/ex2.vcf humandb/ -buildver hg38 -out myanno -remove -protocol refGene,cytoBand,exac03,avsnp147,dbnsfp30a -operation g,r,f,f,f -arg '-hgvs',,,, -nastring . -vcfinput -polish

The txt file generate in this step will be used for the next steps. In the following scripts, only exonic variants will be considered.

#Step 2: Fetch uniprot annotation with gather_uniprot_annotation.py
This script uses a local tsv file containing all human genes from uniprot to annotate de VCF. GOs, Kegg, Reactome and PFAM information will be added to each line of the VCF file

#Step 3: AlphaMissense
The final script finds the variants in the AlphaMissense table of pre-calculated human proteome variants, the pathogenicity information is added to the final dataframe
