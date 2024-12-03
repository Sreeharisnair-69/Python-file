'''
Name: Sreehari Sreekumar Nair
Date: 3 Dec 2024
Purpose: Program that finds the sum of two positive numbers using recursion.
'''
def add_numbers(n1,n2):
    if n2 == 0:
        return n1
    else:
        return add_numbers(n1+1,n2-1)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
f = add_numbers(num1,num2)

print(f"The sum of {num1} and {num2} is {f}")