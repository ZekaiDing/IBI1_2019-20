# -*- coding: utf-8 -*-
"""
Created on Thu May 13 16:09:27 2020

@author: lenovo
"""

sequence = 'ATGCGACTACGATCGAGGGCCAT'
d = {"A":"T","T":"A","G":"C","C":"G"}
rcs=''

for i in sequence:
    rcs +=d[i]

rcs = rcs[::-1]
#reverse
print(rcs)
