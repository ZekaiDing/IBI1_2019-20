# -*- coding: utf-8 -*-
"""
Created on Fri May 14 07:09:15 2020

@author: lenovo
"""

import itertools

print('the number should be an integer from 1 to 23')
a = input('please input the first number:')
b = input('please input the second number:')
c = input('please input the third number:')
d = input('please input the fourth number:')

num=[a,b,c,d]

nlist=[]
[ nlist.append(n) for n in list(itertools.permutations(num)) if n not in nlist]
print(nlist)
# to get the combination

operate = ['+', '-', '*', '/']
oplist= list(itertools.product(operate, repeat=3))
print(oplist)
# to get the Arrangement

#1. (a+b)+(c+d) the'+'only show there should be an operator
solve0= ['('+str(x[0])+y[0]+str(x[1])+')'+y[1]+'('+str(x[2])+y[2]+str(x[3])+')' for x in nlist for y in oplist]

#2. ((a+b)+c)+d
solve1= ['('+'('+str(x[0])+y[0]+str(x[1])+')'+y[1]+str(x[2])+')'+y[2]+str(x[3]) for x in nlist for y in oplist]

#3. (a+(b+c))+d
solve2= ['('+str(x[0])+y[0]+'('+str(x[1])+y[1]+str(x[2])+')'+')'+y[2]+str(x[3]) for x in nlist for y in oplist]

#4. a+((b+c)+d)
solve3= [str(x[0])+y[0]+'('+'('+str(x[1])+y[1]+str(x[2])+')'+y[2]+str(x[3])+')' for x in nlist for y in oplist]

#5. a+(b+(c+d))
solve4= [str(x[0])+y[0]+'('+str(x[1])+y[1]+'('+str(x[2])+y[2]+str(x[3])+')'+')' for x in nlist for y in oplist]

All=[solve0,solve1,solve2,solve3,solve4]

W = False
for n in All:
    for m in n:
        try:
         if eval(m) == 24:
                W = True
                print(m + '=24')
        except:
         pass
#use eval() because it can calculate equation in string
#use try: and except: to take out division by zero
if W == False:
    print ('no answer')





