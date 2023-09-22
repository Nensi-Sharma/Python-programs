pname=input("Enter the name of the product")
cost=int(input("Enter the cost of the product"))
qty=int(input("Enter the Quantity of the product"))
amt=cost*qty
discount=10*amt/100
netamt=amt-discount

print('----------------------')
print('         bill        ')
print('----------------------')
print("product name" , pname)
print("cost        ", cost)
print("quantity    ", qty)
print("amount      ",amt)
print("discount you get",discount)
print("please pay", netamt)
