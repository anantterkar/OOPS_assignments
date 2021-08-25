# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 20:54:34 2021

@author: USER
"""

#printing pattern

def showSigns(rows):
    for i in range(0,rows+1):
        for j in range(1,i+1):
            print("&", end="")
        print("\n")
x = int(input("Give an integer\n"))
showSigns(x)