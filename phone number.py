'''
Name: Sreehari Sreekumar Nair
Date: 30 November 2024
Purpose: Program to check whether the given number is a valid mobile number or
         not using functions.
'''

def phone_number ():
    mob = input("Enter phone number:" )
    if len(mob) == 10 and mob[0] == "7" or mob[0] == "8" or mob[0] == "9":
            print(f"{mob} is a valid phone number")
    else:
        print(f"{mob} is not a valid phone number")

phone_number()