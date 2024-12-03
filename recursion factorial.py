'''
Name: Sreehari Sreekumar Nair
Date: 3 Dec 2024
Purpose: Program that finds the factorial of a given number using recursion.
'''
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

num = int(input("Enter number: "))
f = factorial(num)
print(f"{num} factorial is {f}")
