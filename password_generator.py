# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

letters = ['a', 'b', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
           't', 'u', 'v', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '%', '(', ")", '-', '+', '?']

password = []


while len(password) < 4:
    password.append(random.choice(letters))
while len(password) < 8:
    password.append(random.choice(numbers))
while len(password) < 10:
    password.append(random.choice(symbols))
    
random.shuffle(password)

print("Welcome to Password Generator!")
question = int(input("How many characters do you want in your password? (I can create up to 9 characters) "))
while len(password) < question:
    password.append(random.choice(letters + numbers + symbols))

random.shuffle(password)

for character in password[:question]:
    print(character, end = '')
    
