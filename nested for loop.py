
'''
Name: Sreehari Sreekumar Nair
Date: 19 Nov 2024
Aim: Program to construct patterns of stars (*), using a nested for loop.
'''


star = "*"
rows = int(input("Enter number of rows: "))
print("Increasing Triangle")
for i in range(1,rows+1):
    for j in range(i):
        print("*", end=" ")
    print()


print("\nDecreasing Triangle:")
for i in range(rows,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()


print("\nHill Triangle:")
for i in range(1,rows+1):
    for j in range(rows-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        print("*", end=" ")
    print()


print("\nReverse Hill Triangle:")
for i in range(rows,0,-1):
    for j in range(rows-i):
        print(" ", end=" ")
    for k in range(2*i-1):
        print("*", end=" ")
    print()



