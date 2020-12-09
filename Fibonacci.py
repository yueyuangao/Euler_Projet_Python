#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 21:36:08 2020

@author: yueyuangao

For the Questions concerning Fibonacci sequence
Q2, Q25
"""
import numpy as np
##########################################################################
" Q 2 : "
def Fibonacci_2(i_place):
    """
    Find the Fibonacci number with index i_place
    """
    a1=1
    a2=1
    if i_place == 1:
        return a1
    elif i_place ==2:
        return a2
    else:
        for i in range(2,i_place):
            a1, a2 = a2, a1+a2
    
    return a2


summ=2
sum_track = np.array([])
np.append(sum_track,1)

i =3
while Fibonacci_2(i) <= 4000000:
    print(Fibonacci_2(i))
    if Fibonacci_2(i)%2 ==0:
        summ += Fibonacci_2(i)
        sum_track=np.append(sum_track, summ)
    i=i+1

print(summ)  # To see the exponention increase
print(i)

##########################################################################
" Q 25 : "
import numpy as np
for i in range(1,13):
    print ([i, Fibonacci_2(i), np.floor(np.log10(Fibonacci_2(i)))+1])

i = 12
from decimal import Decimal
while np.floor(np.log10(Decimal(Fibonacci_2(i))))+1<1000:
    i=i+1
print(i)

