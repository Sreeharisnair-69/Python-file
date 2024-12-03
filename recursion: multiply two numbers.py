'''
Name: Sreehari Sreekumar Nair
Date: 3 Dec 2024
Purpose: Program that finds the product of a two numbers using recursion.
'''
def multiply_numbers(n1,n2):

    if n2 == 1:
        return n1
    else:
        return n1 + multiply_numbers(n1,n2-1)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
f = multiply_numbers(num1,num2)
print(f"The product of {num1} and {num2} is {f}")