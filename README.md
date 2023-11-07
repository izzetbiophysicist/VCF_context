# VCF_context

This tool is designed to fetch functional annotations along with AlphaMissense predictions, and generate structures for variants in a VCF file.

## Step 1: Annotate VCF with Annovar
1.1. Use the `table_annovar.pl` script to annotate your VCF file. For example:

# VCF_context

This tool is designed to fetch functional annotations, perform AlphaMissense predictions, and generate structures for variants in a VCF file.

## Step 1: Annotate VCF with Annovar
1.1. Use the `table_annovar.pl` script to annotate your VCF file. For example:

```perl
perl table_annovar.pl example/ex2.vcf humandb/ -buildver hg38 -out myanno -remove -protocol refGene,cytoBand,exac03,avsnp147,dbnsfp30a -operation g,r,f,f,f -arg '-hgvs',,,, -nastring . -vcfinput -polish
```

The resulting text file generated in this step will be used in the subsequent steps. Note that, in the following scripts, only missense variants will be considered.

Annovar can be downloaded from: Annovar Download
## Step 2: Fetch Uniprot Annotation with gather_uniprot_annotation.py

2.1. Use the gather_uniprot_annotation.py script with a local TSV file containing all human genes from Uniprot to annotate the VCF. This will add GOs, BRENDA, and PFAM information to each line of the VCF file.

## Step 3: AlphaMissense

3.1. The final script is designed to find the variants in the AlphaMissense table, which contains pre-calculated human proteome variants. Pathogenicity information is added to the final DataFrame. It is recommended to use a table without commented lines or remarks.

The AlphaMissense table can be downloaded from: AlphaMissense GitHub
Step 4: Creating Structures (Future Updates)

### 4.1. In future updates, the tool will utilize the AlphaFold database and the pyRosetta molecular modeling suite to generate structures for all variants. Stay tuned for more information on this feature.
