# -*- coding: utf-8 -*-
"""
Created on Thu May 13 23:24:02 2020

@author: lenovo
"""

import re

s=''
t=False

rs=[]
d = {"A":"T","T":"A","G":"C","C":"G"}#creat a dictionary
name=''
file=input('please input the file name:')
x=open(file,'w')

DNA = open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')

for line in DNA:
    
    if line.startswith('>'):
        if s != '':
            x.write(name + '      ' +str(len(s)) +'\n' )
            for i in s:
                rs += d[i]#get the reverse complementary sequences of mitochondria genes
           
            rs = rs[::-1]
            rs=''.join(rs)
            x.write(rs+'\n')        
            t=False
            s=''
            j=''
            reseqs=''
        if 'Mito:' in line:
          name=re.findall(r'^>[0-9A-Z]+',line)
          name=''.join(name)
          
          t=True
          s=''             
    else:
        if t==True: 
          line=line.rstrip()
          s += line  
                    
             
x.close()