"""
Author: Sreehari Sreekumar Nair
Date:3 December 2024
Purpose: Program to create monty hall game
"""

print("Welcome to the Monty Hall game", "\nthere are three doors ")

import random
doors=[1,2,3]
host=random.choice(doors)
participant=int(input("Choose door 1, 2 or 3: "))

if participant==host:
    print("You won car")
else:
    print("You chose goat")
    chance2=(input("Do you want to switch your choice? "))
    if chance2=="yes":
        chance3=int(input("Choose another door:"))
        if chance3==host:
            print("you won the car")
        else:
            print("you select goat, you lose")
    else:
        print("you lose")
