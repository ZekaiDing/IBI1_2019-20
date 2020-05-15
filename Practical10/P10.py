# -*- coding: utf-8 -*-
"""
Created on Fri May 15 09:46:16 2020

@author: lenovo
"""

x=''
y=''
z=''
L='ARNDCQEGHILKMFPSTWYVBZX'
s1=0
s2=0
s3=0
d1=0
d2=0
d3=0
import pandas as pd
mousegene=open('SOD2_mouse.fa')
humangene=open('SOD2_human.fa')
randomgene=open('RandomSeq.fa')
blosum= pd.read_csv("BLOSUM62 matrix.csv")

for line in mousegene:
    if not line.startswith('>'):
        x+= line.strip()

for line in humangene:
    if not line.startswith('>'):
        y+=line.strip()

for line in randomgene:
    if not line.startswith('>'):
        z+=line.strip()

def find(a):
    for i in range (0,len(L)):
        if L[i]==a:
            return i


for t in range (0,len(x)):
    s1+= (blosum.loc[find(x[t]),y[t]])
    
print('The final score between mousegene and humangene', s1)

for t in range (0,len(x)):
    s2 += (blosum.loc[find(x[t]),z[t]])

print('The final score between mousegene and randomgene', s2)

for t in range (0,len(y)):
    s3+=(blosum.loc[find(y[t]),z[t]])

print('The final score between randomgene and humangene', s3)


edit_distance = 0 
for i in range(len(y)):
    if y[i]!=x[i]:
        d1 += 1
    if y[i]!=z[i]:
        d2 +=1
    if z[i]!=x[i]:
        d3+= 1

print('The edit diatance between human gene and mouse gene:', d1)
print('The edit diatance between random gene and huaman gene:', d2)
print('The edit diatance between random gene and mouse gene:', d3)





