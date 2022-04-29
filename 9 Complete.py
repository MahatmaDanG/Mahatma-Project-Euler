# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 20:24:14 2021

@author: Mahatma
"""
import math
for a in range(0,332):
    for b in range (a+1,499):
        c = 1000-(a+b)
        ans = (a*a)+(b*b)
        if ans == (c*c):
            print (a,b,c,(a*a),(b*b),(c*c))
            print (a*b*c)
        else:
            ans = 0