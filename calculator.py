operation=input('''
_________________________________________________________

Please select your desired operator to perform the calculation! :
+ for addition
- for subtraction
* for multiplication
/ for division
// for floor division

----------------------------------------------------------

Want to check relational operators? :
> to check greater than
< to check lesser than
>= to check greater than and equal to
<= to check lesser than and equal to
== to check equality
!= to check inequality

___________________________________________________________

''')

n1=int(input("Enter your first number: "))
n2=int(input("Enter your second number: "))

if operation == '+':
    print(n1,"+",n2,"=")
    print(n1+n2)

elif operation == '-':
    print(n1,"-",n2,"=")
    print(n1-n2)

elif operation == '*':
    print(n1,"*",n2,"=")
    print(n1*n2)

elif operation == '/':
    print(n1,"/",n2,"=")
    print(n1/n2)

elif operation == '//':
    print(n1,"//",n2,"=")
    print(n1//n2)

elif operation == '>':
    if n1>n2:
        print('true')
    else:
        print('false')

elif operation == '<':
    if n1<n2:
        print('true')
    else:
        print('false')

elif operation == '>=':
    if n1>=n2:
        print('true')
    else:
        print('false')

elif operation == '<=':
    if n1<=n2:
        print('true')
    else:
        print('false')

elif operation == '==':
    if n1==n2:
        print('true')
    else:
        print('false')

elif operation == '!=':
    if n1!=n2:
        print('true')
    else:
        print('false')

else:
    print("You have not provided a valid operator, please run the program again! :( ")
    
