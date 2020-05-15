# -*- coding: utf-8 -*-
"""
Created on Thu May 14 00:05:54 2020

@author: lenovo
"""

number=input('please input a positive integer:')
number=int(number)

result=''

while number >=1:
  result += str(number) + '-'
  if number == 1:
     break  #when reach 1, end this loop
  elif number % 2 == 0:
       number /= 2
  else:
    number= number*3+1
    
result=result[0:len(result)-1] #remove the last "-"

print(result)

