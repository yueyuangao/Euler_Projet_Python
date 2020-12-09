#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 21:36:08 2020

@author: yueyuangao
"""
import numpy as np

def prime(n):
    if n ==2:
        return 1
    diviser = int(np.sqrt(n))+1    
    #print (diviser)
    for i in range(2,diviser+1):
        if n % i ==0:
            return 0
    
    return 1   

def prime_factor_3(n):
    if n < 3:
        print ("n is small")
        return 1
    else :
        diviser = int(n/2)  
        #print (diviser)
        for i in range(2,diviser+1):
            if prime(i)==1 and n % i ==0:
                n =n/i
                print ([i,n])
                if i>n:
                    break
                
def sum_prime_10(n):
    summation =0
    for i in range (2,n+1):
        if prime(i) == 1:
            summation+=i
    print(summation)
    return summation

#########################################
import matplotlib.pyplot as plt
rg =np.random.default_rng()
rg.normal(20,2,1)
N=1000000
sample_question = rg.normal(20,2,N)
plt.hist(sample_question,density=1)
sum_1 =0
sum_2 =0
for i in range(0,N):
    if sample_question[i]<19.5:
        sum_1 +=1
    if sample_question[i]<22 and sample_question[i]>20:
        sum_2 +=1
print ([sum_1, sum_1/N])
print ([sum_2, sum_2/N])

###########################################
def Fibonacci_2(i_place):
    a1=1
    a2=2
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

print(summ)
print(i)


if __name__ == '__main__':
    n = int(input().strip())
    print (n)
    
if __name__ == '__main__':
    n = int(input())
    for i in range(1,n):
        print(i*i)
        
        
        
def is_leap(year):
    leap = False
    if year % 100 ==0:
        if year % 400 == 0:
            leap =True
    else:
        if year % 4 ==0:
            leap = True
    # Write your logic here
    
    return leap



arr = list(map(int, input().rstrip().split())) 
