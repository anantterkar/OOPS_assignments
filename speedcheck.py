# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 20:16:21 2021

@author: USER
"""

#speedlimit
def speedcheck(speed):
    if(speed<=70):
        print("OK\n")
    else:
        print("Points:",(speed-70)/5)

car_speed = int(input("Give an integer speed of car in km\n"))
speedcheck(car_speed)