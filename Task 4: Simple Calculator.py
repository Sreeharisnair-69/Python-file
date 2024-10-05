'''
Author: Sreehari Sreekumar Nair
Date: 5 October 2024
Purpose: To write a Python program that can perform square root, factorial and exponent
         calculations
'''

number = int(input("Enter a number:"))

import math
sqrt = math.sqrt(number)
factorial = math.factorial(number)
power = math.pow(number,2)

print("\n\nSquare root of",number,":",sqrt,"\n\nFactorial of",number,":",factorial,
      "\n\n",number," raised to power 2:",
      power)
