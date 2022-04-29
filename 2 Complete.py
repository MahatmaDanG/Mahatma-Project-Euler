# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 17:20:02 2021

@author: Mahatma
"""

a = 1
b = 1
c = 0
Below = True
Allowed = []
while Below == True:
    print(a,b,c)
    c = a + b
    if c <= 4000000:
        if c % 2 == 0:
            Allowed.append(c)
        a = b
        b = c
        
    else:
        Below = False
    # print(c)
    # a = b
    # b = c
    # print(a,b,c)
    # Below = False
print(Allowed)    
print(sum(Allowed))