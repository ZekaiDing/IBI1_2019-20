# -*- coding: utf-8 -*-
"""
Created on Thu May 13 21:43:17 2020

@author: lenovo
"""

import re

x=''
t=False
name=''
sequence=[]

DNA = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
file= open('mito_gene.fa','w')

for line in DNA:    
    if line.startswith('>'):
        if x != '':
            sequence.append(x)
            n = re.search(r'(gene):(\w+)',line)
            name = n.group(2)
            file.write('\n'+name + '      ' +str(len(x)) +'\n')
            t=False
            x=''
        if 'Mito:' in line:
          name=re.findall(r'^>[0-9A-Z]+',line)
          name=''.join(name)
          t=True
          x='' 
    else:
        if t==True: 
          line=line.strip()
          x += line
          
file.close()

