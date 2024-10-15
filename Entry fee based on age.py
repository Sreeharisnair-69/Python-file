'''
Name: Sreehari Sreekumar Nair
Date: 15 October 2024
Purpose: A program to calculate entry fee based on age.
'''

age = int(input("Enter your age:"))

if(age < 10):
    print("Entry fee is 7")

elif(age >= 10 and age <= 60):
    print("Entry fee is 10")

else:
    print("Entry fee is 5")