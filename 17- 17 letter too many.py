# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 16:30:03 2021

@author: Mahatma
"""

def Ones(digs):                          # Computes the length for the tenths an hundreths postions 
    global total
    #print (digs)
    if digs == "1" or digs == "2" or digs == "6":
        total += 3
    elif digs == "4" or digs == "5" or digs == "9":
        total += 4
        #print ("present")
    elif digs == "3" or digs == "7" or digs == "8":
        total += 5
        
def Teen(unos):
    global total
    if unos == "0":
        total += 3
    elif unos == "1"or unos == "2":
        total += 6
    elif unos == "5"or unos == "6"or unos == "9":
        total += 7
    elif unos == "3"or unos == "4"or unos == "8":
        total += 8
    elif unos == "7":
        total += 9
        
def Tens(noom):
    global total
    if noom == "2"or noom == "3" or noom == "8" or noom =="9":
        total += 6
    elif noom == "4" or noom == "5" or noom == "6":
        total += 5
    if noom == "7":
        total += 7

total = 11
for loop in range (1,1000):
    num = str(loop) 
    last = total
    if len(num) == 1:
       Ones(num)
    if len(num)>= 2:   
        if num [-2] != "1":                  # Because teen numbers dont follow the rules
            Ones(num[-1])
        else:
            Teen(num[-1])
    if len(num) == 3:
        if num[-1] or num[-2] != "0":
            total += 10
        else:
            total += 7
        Ones(num[0])
    if  len(num)>= 2 and num [-2] != "1":
        Tens(num[-2]) 
    if last - total == 6:
        print (num,total)
    #print (total)
print (total)          
                
        
        
        
        
        
        # one two three four five six seven eight nine
        # ten eleven twelve thirteen fourteen fifteen 
        # sixteen seventeen eighteen ninteen
        # twenty thirty forty fifty sixty seventy eighty ninety
        