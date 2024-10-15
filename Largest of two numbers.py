'''
Name: Sreehari Sreekumar Nair
Date: 15 October 2024
Purpose: A program to find the largest of two numbers
'''

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

if(num1 > num2):
    print(num1,"is larger")

elif(num2 > num1):
    print(num2,"is larger")

else:
    print(num1,"is equal to",num2)