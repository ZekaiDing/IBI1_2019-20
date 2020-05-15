# -*- coding: utf-8 -*-
"""
Created on Thu May 14 11:28:03 2020

@author: lenovo
"""

gene_lengths=[9410,3944141,4442,105338,19149,76779,126550,36296,842,15981]
gene_lengths.sort()#sort from smallest to biggest

del(gene_lengths[0])#delete the smallest one
del(gene_lengths[8])#delete the biggest one

import matplotlib.pyplot as plt
plt.boxplot(gene_lengths,vert=True,showbox=True,patch_artist=True)
plt.show()
#draw the boxplot