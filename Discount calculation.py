'''
Name: Sreehari Sreekumar Nair
Date: 15 October 2024
Purpose: A program to calculate discount of a bill amount.
'''

bill_amount = float(input("Enter bill amount:"))

if(bill_amount > 500):
    print("Total amount is:",0.8 * bill_amount)

elif(200 <= bill_amount <= 500):
    print("Total amount is:",0.9 * bill_amount)

else:
    print("Total amount is:",bill_amount)