'''
Name: Sreehari Sreekumar Nair
Date: 15 October 2024
Purpose: A program to find the sum of the digits of a number.
'''

num = int(input("Enter a number:"))

sum = 0

while(num > 0):
    rem = num % 10
    num = num // 10
    sum = sum + rem

print("The sum of the digits is:",sum)
