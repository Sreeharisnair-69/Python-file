'''
Name: Sreehari Sreekumar Nair
Date: 3 Dec 2024
Purpose: Program that finds the GCD of two numbers using recursion.
'''

def gcd(n1,n2):
    if n1 % n2 == 0:
        return n2
    else:
        return gcd(n2,n1 % n2)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
gcd = gcd(num1,num2)

print(f"The GCD of {num1} and {num2} is {gcd}")