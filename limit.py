# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 20:29:41 2021

@author: USER
"""

def showNumbers(limit):
    for i in range(0,limit+1):
        if(i%2==0):
            print(i,"EVEN\n" )
        else:
            print(i, "ODD\n" )
            
x = int(input("Give an integer\n"))
showNumbers(x)