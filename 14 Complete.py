# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 13:11:39 2021

@author: Mahatma
"""
import time
start = time.process_time()



attempt = 1
xB = 1
x = 1
length = [0,1,[]] 
LengthTest = 0
Max = 1000000
while xB < 1000000:
    x = xB
    LengthTest = [0,[]]
    while x != 1:
        if x % 2 == 0:
            x = x/2
            LengthTest[0] += 1
            LengthTest[1].append(x)
        else:
            x = (3*x)+1
            LengthTest[0] += 1
    if LengthTest[0] > length[1]:
        length [0] = xB
        length [1] = LengthTest[0]
        length [2] = LengthTest[1]
    attempt += 1
    xB = 2*attempt - 1
if length[0]< (Max/2)+1:
    Length[0] = (Length [0])*2
    length [1] += 1
    Length[2].insert(Length[0],0)
print(length)

   
print(time.process_time() - start)