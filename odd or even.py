'''
Name: Sreehari Sreekumar Nair
Date: 19 Nov 2024
Purpose: Program to take two lists of numbers from the user and merge them.
The merged list should be sorted with even numbers first and then odd, both in ascending order.
'''

list1=[]
list2=[]

list1_size=int(input("Enter the size of a list1:"))
print("Enter the elements of list1")
for i in range(list1_size):
    list1.append(int(input()))
print("list 1: ", list1)

list2_size=int(input("Enter the size of list2:"))
print("Enter the element in list2:")
for i in range(list2_size):
    list2.append(int(input()))
print("list 2: ", list2)

combined_list=list1+list2
print("Combined list: ", combined_list)

even_list=[]
odd_list=[]

for i in combined_list:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

even_list.sort()
print("Even list: ", even_list)

odd_list.sort()
print("Odd list", odd_list)

merged_list=even_list+odd_list
print("Merged list: ", merged_list)
