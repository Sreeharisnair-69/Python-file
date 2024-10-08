'''
Author: Sreehari Sreekumar Nair
Date: 08 October 2024
Purpose: To perform addition, subtraction, multiplication,
         division and modulus calculations.
'''

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

sum = num1 + num2
print("The sum of num1 and num2 is:",sum )

difference = num1 - num2
print("The difference when num2 is subtracted from num1 is: ", difference)

product = num1 * num2
print("The product of num1 and num2 is: ",product)

quotient = num1 / num2
print("The quotient when num1 is divided by num2 is: ",quotient)

modulus = num1 % num2
print("The remainder when num1 is divided by num2 is: ", modulus)

composite = (num1 + num2) * num3 / 2
print("The result of (",num1, "+", num2,") *", num3, "/ 2 is: ", composite)