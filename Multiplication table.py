'''
Name: Sreehari Sreekumar Nair
Date: 29 October 2024
Purpose: To create a table that shows the first 12 multiples of a given number
'''
number = int(input("Enter a number: "))
for i in range(1,13):
    product = number * i
    print(f"{number} x {i} = {product}")
