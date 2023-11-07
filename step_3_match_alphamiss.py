#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 17:38:03 2023

@author: lucas
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 10:12:25 2023

@author: lucas
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 15:04:46 2023

@author: lucas
"""
import pandas as pd
import ast
import logging

### Match AlphaMissense

tsv_file = 'alphamiss_noRemarks.tsv'

final = pd.read_csv('teste.csv')
all_uniprots=[x.replace("'", "") for x in final['uniprot_IDs']]
all_uniprots=[x[1:-1].replace("'", "").split(', ')[0] for x in final['uniprot_IDs']]

all_mutations = [x[1:] for x in final['mutation']]

pairs = [x+','+y for x, y in zip(all_uniprots, all_mutations)]

c=0
out_file = '/home/lucas/annovar_test/alphamiss_filter.tsv'

with open(tsv_file, 'r') as input_file:
    with open(out_file, 'w') as output_file:
        
        for line in input_file:
            c=c+1
            # Split the line into columns based on the delimiter (in this case, '\t' for TSV)
            print(c/216175352)
            columns = line.strip().split('\t')
            uniprot_ID = columns[0]  
            variant = columns[1][1:]
            
            if uniprot_ID+','+variant in pairs:
                output_file.write(line)  # Write the line to the output file
                
    


