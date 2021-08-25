# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 21:10:57 2021

@author: USER
"""

def prime(x):
    cnt=0
    for i in range(2,x):
        if(x%i==0):
            cnt+=1
    if(cnt>0):
        return 0
    else:
        return 1

def printPrime(max):
    for i in range(2,max+1):
        if(prime(i)==1):
            print(i)
c = int(input("GIve an integer\n"))
printPrime(c)