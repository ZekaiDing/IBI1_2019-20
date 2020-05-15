# -*- coding: utf-8 -*-
"""
Created on Thu May 14 00:36:49 2020

@author: lenovo
"""

a = 123
b = 123123
c = b % 7
d = c % 11
e = d % 13
print ('e =',e)

if a < e:
    print('a < e')
elif a > e:
    print('a > e')
else:
    print('a = e')
#e is eestimated to become 0. Because 123123/7 = 0, then d and e will become 0

X = True
Y = True

Z = (X	and	not	Y)	or	(Y and	not	X)
W = X != Y
print('When X is True and Y is True, Z is',Z,', W is',W ) 

X = False
Y = True
Z = (X	and	not	Y)	or	(Y and	not	X)
W = X != Y
print('When X is Flase and Y is True, Z is',Z,', W is',W ) 

X = False
Y = False
Z = (X	and	not	Y)	or	(Y and	not	X)
W = X != Y
print('When X is Flase and Y is Flase, Z is',Z,', W is',W )

X = True
Y = False
Z = (X	and	not	Y)	or	(Y and	not	X)
W = X != Y
print('When X is True and Y is Flase, Z is',Z,', W is',W )