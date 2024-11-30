'''
A program that accepts the lengths of three sides of a triangle as inputs.
The program should output whether or not the triangle is a right triangle
(Recall from the Pythagorean Theorem that in a right triangle, the square
of one side equals the sum of the squares of the other two sides).
Implement using functions.
'''

def triangle():
    side1 = int(input("Enter the length of first side: "))
    side2 = int(input("Enter the length of second side: "))
    side3 = int(input("Enter the length of third side: "))
    dimensions = [side1,side2,side3]
    dimensions.sort()
    if dimensions[2]**2== (dimensions[0]**2 +dimensions[1]**2):
        print("Given triangle is a right triangle")
    else:
        print("Given triangle is not a right triangle")

triangle()


