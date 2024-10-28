# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 21:07:25 2024

@author: user
"""

to_do_list = []
while True:
    desire = input("Add tasks (t), view tasks (v), remove task (r), quit (quit)\n>>> ").lower()
    if desire == 't':
        print("You can add your tasks here (To stop, type 'quit')")
        while True:
            task = input(">>> ")
            if task == 'quit':
                break
            to_do_list.append(task)
        print("Your tasks are saved!")
    elif desire == 'v':
        if not to_do_list:
            print("You have no tasks yet.")
        else:
            for t in to_do_list:
                print(t)
    elif desire == 'r':
        print("Write '+' for tasks you want to remove. For others, '-' :")
        to_do_list_copy = to_do_list.copy()  # Create a copy for safe removal
        for task in to_do_list_copy:
            response = input(f"{task} >>> ")
            if response == '+':
                to_do_list.remove(task)
    elif desire == 'quit':
        break
