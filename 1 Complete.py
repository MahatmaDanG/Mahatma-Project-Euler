# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 16:57:09 2021

@author: Mahatma
"""

import math

All = list(range(1000))

Sum = []
for number in All:
    if number % 3 == 0:
        Sum.append(number)
    elif number % 5 == 0:
        Sum.append(number)
Ans = sum(Sum)
print(Ans)

        