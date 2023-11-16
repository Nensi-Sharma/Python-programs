num = int(input("enter a number: "))
if num==1:
    print("prime number")
else:
    f=0
    for a in range(2,num):
        if num%a==0:
            f=1
            break
    if f==0:
        print("number is prime")
    else:
        print("composite number")
