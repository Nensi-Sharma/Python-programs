print("Hello there! :)")
print(" Here's a fun program to input the 3 sides of a triangle and find out if its equilateral, isoscles or scalene")      
x=int(input("enter the length of the first side of the triangle: "))
y=int(input("enter the length of the second side of the triangle: "))
z=int(input("enter the length of the third side of the triangle: "))
if x==y==z:
      print("the triangle is equilateral!")
elif x==y or x==z or z==y:
      print("the triangle is isoscles!")
else:
    print("the triangle is scalene!")
print("have a good day!  :)")
