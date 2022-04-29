# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 18:51:30 2021

@author: Mahatma
"""

# primes = []
# target = 600851475143
# Numbers = []
# for x in range(3,int(target/2)):
#     print(x)
#     for y in range(2,(x-1)):
#         print(y)
#         if x % y == 0:
#             break
        
#     primes.append(x) 
# print(primes)   

import math
#squares = [2]
target = 600851475143
factors = []
factoring = True
Div = False
while factoring == True:
    for n in range (3,2000000,2):
        for x in range (2,int(math.sqrt(n)+1)):
            if n % x == 0:
                break
        else:
            Div = True
            while Div == True:
                if target % n == 0:
                    target = target/n
                    factors.append(n)
                else:
                    Div = False
        if target < 2*n:
            factors.append(target)
            factoring = False
    
        #squares.append(n)
#Total = sum(squares)
#print(Total)
print(factors)
print (target) 