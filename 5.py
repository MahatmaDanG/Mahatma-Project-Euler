# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 13:33:32 2021

@author: Mahatma
"""
# Loop = True
# n = 2520
# Score = 0
# Tried = 0
# while Loop == True:
#     Score = 0
#     for x in range(1,21):
#         if n % x == 0 and (n/x)%2 == 0:
#             Score += 1
#         if Score == 20:
#             print (n)
#             Loop = False
#     n += 1
#     Tried += 1
#     if Tried % 10 == 0:
#         print (Tried)


# primes = []

# for loop in range (2,11):
    
#     for x in range (2,(loop-1),1):
#         if loop % x == 0:
#             break
#         primes.append(loop)
# print(primes)
# #for loop in range(1,21):
    
primes = [2,3,5,7,11,13,17]
for loop in range (2,21):
    y = loop
    for x in range (len(primes)):
        
        if y % primes[x] == 0:
            y = y/primes[x]
            Factors(loop).append(primes[x])

  