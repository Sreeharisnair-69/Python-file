'''
Name: Sreehari Sreekumar Nair
Date: 03 Dec 2024
Purpose: Function that prints Fibonnacci series up to a given number.
'''
def fibonnacci(n):
    first_number = 1
    second_number = 0
    third_number = 0
    while(third_number <= n):
        print(third_number,end = " ")
        third_number = first_number + second_number
        first_number = second_number
        second_number = third_number