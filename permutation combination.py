# python program to find factorial of a given number and use it to find permutation and combination for a given value of (n,r)
n= int(input("enter n: "))
r= int(input("enter r: "))
b=1
c=1
d=1
if n >= 0 and r >= 0 and n >= r:
    for i in range(1, n + 1):
        b*= i

    for j in range(1, r + 1):
        c*= j

    for k in range(1, n - r + 1):
        d*= k
permuatation=b/d
combination=b/(d*c)
print("permuatation",permuatation)
print("combination", combination)
