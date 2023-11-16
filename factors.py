n=int(input("Enter a number: "))
c=0
a=1
while a<=n:
    if n%a==0:
        print(a)
        c+=1
    a+=1
print("number of factors is",c)
if c==2:
    print(n,"is a prime number")
else:
    print(n,"is a composite number")
