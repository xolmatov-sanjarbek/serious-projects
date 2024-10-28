# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:13:11 2024

@author: user
"""

print("Unit converter")
print("K for kilometer to mile, M for mile to kilometer, Q to quit")

while True:
    choose = input("Enter your choise : ").lower()

    if choose == 'k':
        kilometer = float(input("Enter : "))
        print(f"{kilometer} km = {kilometer * 1.6} miles")

    elif choose == 'm':
        miles = float(input("Enter : "))
        print(f"{miles} miles = {miles*0.62} km")
    elif choose == 'q':
        break
    else:
        print("Enter a valid input")
    
