'''
Name: Sreehari Sreekumar Nair
Date: 30 November 2024
Purpose: To calculate the number of upper case and lower case letters in a given string.
'''

def letters():
    string = input("Enter a string: ")
    upper_count = 0
    lower_count = 0

    for i in string:
        if i.isupper():
            upper_count += 1
        if i.islower():
            lower_count += 1
    print(f"Upper count is {upper_count}")
    print(f"Lower count is {lower_count}")

letters()
