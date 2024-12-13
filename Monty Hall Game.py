'''
Author: Sreehari Sreekumar Nair
Date: 13 December 2024
Purpose: Program to create monty hall game
'''

print("Welcome to the Monty Hall game, there are three doors ")

import random
doors = [1,2,3]
host = random.choice(doors)
participant = int(input("\nChoose door 1, 2 or 3: "))

choice = (input("\nDo you want to switch your choice? "))

if choice == "yes":
    chance2 = int(input("\nChoose another door:"))
    if chance2 == host:
        print("\nYou won the car")
    else:
        print("\nYou selected a goat, you lose")

elif choice == "no":
    if participant == host:
        print("\nYou have won the car")
    else:
        print("\nYou selected a goat, you lose")
