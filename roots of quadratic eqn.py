import math
a= int(input('enter number a : '))
b= int(input('enter number b : '))
c= int(input('enter number c : '))
d=b**2-4*a*c
if d>0:
    print("real and not equal roots")
    x = (-b + math.sqrt(d))/(2*a)
    y = (-b - math.sqrt(d))/(2*a)
    print( "root 1: ",x,"and root 2: ",y)
elif d==0:
    print("real and equal roots")
    x = (-b + math.sqrt(d))/(2*a)
    y = (-b - math.sqrt(d))/(2*a)
    print( "root 1: ",x,"and root 2: ",y)
else:
    print("real and imaginary")
    x = (-b + math.sqrt(d))/(2*a)
    y = (-b - math.sqrt(d))/(2*a)
    print( "root 1: ",x,"and root 2: ",y)
    
    
