# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 14:50:39 2021

@author: Mahatma
"""
num = 2
total = 0
inp = int(input("power? "))
for loop in range(inp-1):
    num = num*2
print(num)
dig = str(num)
for loop in range (len(dig)):
    total += int(dig[loop])
print (total)