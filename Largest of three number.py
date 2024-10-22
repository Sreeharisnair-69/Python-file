'''
Name: Sreehari Sreekumar Nair
Date: 22 October 2024
Purpose: A Python program to find the largest of three numbers.
'''

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
num_3 = int(input("Enter third number: "))

if(num_1 > num_2 and num_1 > num_3):
    print(num_1, "is largest")

elif(num_2 > num_1 and num_2 > num_3):
    print(num_2, "is largest")

elif(num_3 > num_1 and num_3 > num_2):
    print(num_3, "is largest")

else:
    print("Two or all numbers are equal")