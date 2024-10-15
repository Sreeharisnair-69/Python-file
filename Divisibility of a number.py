'''
Name: Sreehari Sreekumar Nair
Date: 15 October 2024
Purpose: A program to check whether a number is divisible by another number.
'''

dividend = float(input("Enter dividend:"))
divisor = float(input("Enter divisor:"))

if(dividend % divisor == 0 ):
    print(dividend,"is divisible by",divisor)

else:
    print("Not divisible")
