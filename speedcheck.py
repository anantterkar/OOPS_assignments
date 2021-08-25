# -*- coding: utf-8 -*-
"""
Created on Wed Aug 25 20:16:21 2021

@author: USER
"""

#speedlimit
def speedcheck(speed):
    if(speed<=70):
        print("OK\n")
    elif((speed-70)/5<12):
        print("Points:",(speed-70)/5)
    else:
        print("License suspened\n")

car_speed = int(input("Give an integer speed of car in km\n"))
speedcheck(car_speed)