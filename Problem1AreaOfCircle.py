# Muhammad Haroon Nasir
# 05/09/25
# Problem 1: A function areaOfCircle(r) which returns the area of a circle of radius r. r is a user input value

import math

# Function to compute area of a circle
def areaOfCircle(r):
    area = math.pi * (r ** 2)

    return area

# Example use
radius = float(input("Enter the radius of the circle: "))
print(f"The area of the circle is: {areaOfCircle(radius)}")