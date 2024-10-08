'''
Author: Sreehari Sreekumar Nair
Date: 08 October 2024
Purpose: A program that performs the following tasks:

    Create two separate strings:
        The first string should contain your first name.
        The second string should contain your last name.

    Concatenate the two strings with a space in between and store the result in a
    new variable.

    Print the concatenated string.

    From the concatenated string:
    Access and print a sub-string that consists of the first name only.
    Use string slicing to extract the sub-string.
    '''

first_name = str(input("Enter first name: "))
last_name = str(input("Enter last name: "))
full_name = first_name + " " + last_name

print(full_name)
length = len(first_name)
extracted_first_name = full_name[0:length]
print(extracted_first_name)

