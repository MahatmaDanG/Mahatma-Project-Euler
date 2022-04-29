# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 13:13:26 2021

@author: Mahatma
"""
m = 0
n = 0
t = 0
Ans = 0
for x in range (1000,0,-1):
    for y in range (1000,1,-1):
        m = x*y
        n = int(str(m)[::-1])
        if m == n:
            t = n
            if t > Ans:
                Ans = t
print(Ans)