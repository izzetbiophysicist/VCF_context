#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 20:17:43 2023

@author: lucas
"""

import pandas as pd
import re
import numpy as np

from unipressed import UniprotkbClient, UniparcClient
import time
from unipressed import IdMappingClient
import pandas as pd
import requests

anno = pd.read_csv('/home/lucas/annovar_test/annovar/annovar_vcf.txt', sep='\t')
human_uniprot = pd.read_csv('/home/lucas/annovar_test/uniprotkb_homo_sapiens_AND_model_organi_2023_11_01.tsv', sep='\t')
human_uniprot['Gene Names']


def extract_exonic_variants(annovar_dataframe):

    gene = []
    mutations = []
    for i in range(np.shape(annovar_dataframe)[0]):
        
        if annovar_dataframe['Func.refGene'][i] == 'exonic' and annovar_dataframe['ExonicFunc.refGene'][i] == 'nonsynonymous SNV':
        
            line = annovar_dataframe['AAChange.refGene'][i]
                
            # Use regular expression to extract the protein change without 'p.'
            match = re.search(r'p\.([A-Za-z*]+)(\d+)([A-Za-z*]+)', line)
            
            if match:
                
                amino_acid_change = match.group(1) + match.group(2) + match.group(3)
    
                gene.append(annovar_dataframe['Gene.refGene'][i])
                mutations.append(amino_acid_change)
                    
                print("Amino Acid Change:", amino_acid_change)
            else:
                print("Amino acid change not found in the line.")
        
    return gene, mutations

def match_uniprot(gene_list, human_uniprot):
    all_matches = []
    for g in gene_list:
        print('Finding uniprot ID for gene '+g)
        matches = []
        for h in range(len(human_uniprot)):
            if str(human_uniprot['Gene Names'][h]) != 'nan':
                if any(item in human_uniprot['Gene Names'][h].split() for item in g.split(';')):
                    matches.append(human_uniprot['Entry'][h])
        all_matches.append(matches)
        
    return all_matches
        
def compile_annotation(exonic, human_uniprot):
    
    data = {
        'gene': exonic[0],
        'mutation': exonic[1],
        'uniprot_IDs': matched_IDs
     }
    
    GO_molecular_function = []
    GO_biological_process = []
    GO_cellular_component = []
    Pfam = []
    AlphaFoldDB = []
    
    for m in data['uniprot_IDs']:
        print('Retrieving annotation for gene ' + m)
        c = 0
        for u in range(len(human_uniprot['Entry'])):
            if any(entry in human_uniprot['Entry'][u] for entry in m):
                c=1
                
                GO_molecular_function.append(human_uniprot['Gene Ontology (molecular function)'][u])
                GO_biological_process.append(human_uniprot['Gene Ontology (biological process)'][u])
                GO_cellular_component.append(human_uniprot['Gene Ontology (cellular component)'][u])
                AlphaFoldDB.append(human_uniprot['AlphaFoldDB'][u])
                Pfam.append(human_uniprot['Pfam'][u])
                break
        
        if c==0:
            GO_molecular_function.append('nan')
            GO_biological_process.append('nan')
            GO_cellular_component.append('nan')
            AlphaFoldDB.append('nan')
            Pfam.append('nan')
                
                
    
    data['GO_molecular_function'] = GO_molecular_function
    data['GO_biological_process'] = GO_biological_process
    data['GO_cellular_component'] = GO_cellular_component
    data['Pfam'] = Pfam
    data['AlphaFoldDB'] = AlphaFoldDB
    final = pd.DataFrame(data)
    
    return final

exonic = extract_exonic_variants(anno)
matched_IDs = match_uniprot(exonic[0], human_uniprot)    
final = compile_annotation(exonic, human_uniprot)

final.to_csv('/home/lucas/annovar_test/teste.csv')
