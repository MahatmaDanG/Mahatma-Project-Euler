# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 22:07:15 2022

@author: Mahatma
"""


def MemberCheck(Unused):
    for n in range(6):
        x = n+3
        if x in Unused:
            Figurate(x)
MemberCheck()

def Figurate(n):
    if n = 3:
        return((n+1)/2)
    elif n == 4:
        return(n)
    elif n == 5:
        return((3n-1)/2)
    elif n == 6:
        return(2n-1)
    elif n == 7:
        return((5n-3)/2)
    elif n == 8:
        return(3n-2)