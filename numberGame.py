# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 19:51:21 2021

@author: USER
"""

#numGame
def numberGame(a):
    if(a%3==0 and a%5!=0):
        print("number")
    if(a%5==0 and a%3!=0):
        print("Game")
    if(a%5==0 and a%3==0):
        print("numberGame")

x = int(input("Give an integer number\n"))
numberGame(x)

        
    