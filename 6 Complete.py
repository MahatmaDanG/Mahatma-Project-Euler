# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 19:50:21 2021

@author: Mahatma
"""

Num = 0
Square = 0 
for x in range (1,101):
    Num += x
    Square += (x*x)
Num = Num*Num
print(Num,Square)
print(Num-Square)
