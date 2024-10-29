'''
Name: Sreehari Sreekumar Nair
Date: 29 October 2024
Purpose: To print the number of vowels and consonants in a given string
'''

str_in = input("Enter a string:")
vowels = "aeiouAEIOU"
cons = "qQwWrRtTyYpPsSdDfFgGhHjJkKlLzZxXcCvVbBnNmM"
vowel_count = 0
cons_count = 0

for char in str_in:
    if char in vowels:
        vowel_count += 1

    else:
        cons_count += 1

print(f"Number of vowels is {vowel_count}")
print(f"Number of consonants is {cons_count}")

