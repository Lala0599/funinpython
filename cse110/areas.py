#core requirements

#area of a square
side = float(input("What is the length of the side of your square? : "))
area = side ** 2

print(f"The area of your square is: {area}")

#area of a rectangle

length = float(input("What is the length of your rectangle? : "))
width = float(input("What is the width of your rectangle? : "))
area_r = length * width

print(f"The area of your rectangle is: {area_r}")

#area of a circle

radius = float(input("What is the radius of the circle? : "))
area_c = 3.14 *(radius ** 2)

print(f"The area of your circle is: {area_c}")

#stretch challenge
import math

#area of a circle using math.pi

radius_2 = float(input("What is the radius of the circle? : "))
area_c_2 = math.pi * (radius ** 2)

print(f"The area of the circle is: {area_c_2}")