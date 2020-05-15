# -*- coding: utf-8 -*-
"""
Created on Thu May 14 10:20:02 2020

@author: lenovo
"""
import matplotlib.pyplot as plt
c_A=int(input('please input the number of A occurs in specific DNA sequence:'))
c_C=int(input('please input the number of C occurs in specific DNA sequence:'))
c_T=int(input('please input the number of T occurs in specific DNA sequence:'))
c_G=int(input('please input the number of G occurs in specific DNA sequence:'))

count = c_A+c_C+c_T+c_G#to get the sum of nucleotides
sA=c_A/count*100
sC=c_C/count*100
sT=c_T/count*100
sG=c_G/count*100
#show the percentages of each kind of nucleotide in the sequence

labels = 'A','C','T','G'
size=(sA,sC,sT,sG)
explode=(0,0,0,0)
plt.title('pie of the four DNA nucleotides')
plt.pie(size,explode=explode,labels=labels,autopct='%1.0f%%',shadow=False,startangle=90)
plt.axis('equal')
plt.show()
#draw the pie-chart

D={'A':sA/100,'C':sC/100,'T':sT/100,'G':sG/100}#creat a dictionary
print (D)
    
        
