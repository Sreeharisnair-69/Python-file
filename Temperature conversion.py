'''
Name: Sreehari Sreekumar Nair
Date: 22 October 2024
Purpose: A Python program to convert temperature values back and forth between Celsius and
         Fahrenheit.
'''

temp_in = float(input("Enter temperature: "))
unit = input("Is this in (C)elsius or (F)ahrenheit? ")

if (unit == "C" or unit == "c"):
    temp_out = (temp_in) * 9 / 5 + 32
    print(temp_in, "Celsius is", temp_out, "Fahrenheit.")

elif (unit == "F" or unit == "f"):
    temp_out = (temp_in - 32) * 5 / 9
    print(temp_in, "Fahrenheit is", temp_out, "Celsius.")

else:
    print("Please enter temperature either in Celsius (C/c) or Fahrenheit (F/f).")
