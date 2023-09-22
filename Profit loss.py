sp=int(input("Enter the selling price: "))
cp=int(input("Enter the cost price: "))
if sp>cp:
    print("Profit is Rs.", sp-cp)
elif cp>sp:
    print("Loss is Rs.", cp-sp)
else:
    print("there is neither Profit, nor Loss!")
