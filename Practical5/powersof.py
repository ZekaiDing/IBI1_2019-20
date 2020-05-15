# -*- coding: utf-8 -*-
"""
Created on Thu May 14 09:37:58 2020

@author: lenovo
"""

#I decided to convert this number to binary where every digit has corresponding power of 2.
number = int(input('please input a positive number (<8192):'))
result = str(number) + 'is'
binary = bin(number)
binary = binary[2:]
for i in range(len(binary)):
    y = binary[i]
    if y == '1':
        result += '2**' + str(len(binary)-i-1) + '+'

result=result[0:len(result)-1]

print(result)
