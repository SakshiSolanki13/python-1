radius=float(input("enter radius of the circle:"))
area=3.14 * radius * radius
circum=2*3.14*radius
print("area of cicle is",area)
print("circumference of circle is",circum)

side=float(input("enter side of the square:"))
area= side * side
per= 4 * side
print("area of square is",area)
print("perimeter of square is",per)

length=float(input("enter the length of the rectangle :"))
breadth=float(input("enter the breadth of rhe rectangle :"))
area= length*breadth
per=2*(length+breadth)
print("area of rectangle is",area)
print("perimeter of rectangle is",per)

import math
side1=float(input("enter side1 of the triangle :"))
side2=float(input("enter side2 of the triangle :"))
side3=float(input("enter side3 of the triangle :"))
s=(side1+side2+side3)/2
area= math.sqrt(s*(s-side1) * (s-side2) * (s-side3))
per= side1+side2+side3
print("area of triangle is",area)
print("perimeter of triangle is",per)