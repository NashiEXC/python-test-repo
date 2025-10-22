#^q^

menuruntime= 1
totalprice= 0


while menuruntime == 1:
    
    print("Menu\t")
    print("0) buy burger\t1) buy drink")

    try:
        ordernum = int(input("enter your order number"))
    except ValueError:
        print("invalid, please try again")
        continue

    if ordernum > 1:
        print("invalid, please try again")
        continue

    orderamt = int(input("enter num of orders: "))

    for i in range(1, orderamt+1):
        
        if ordernum == 0:
            orderprice= float(input(f"how much for burger {i}: "))
            totalprice += orderprice
        else:
            orderprice= float(input(f"how much for drink {i}: "))
            totalprice += orderprice
            
    
    print(f"total is ${totalprice}")
        
        

    YN = input("do you have anymore orders? (Y or N): ").lower()  # Convert input to lowercase

    if YN == "y":
        pass
    elif YN == "n":
        break

print(f"Thank you, please pay ${totalprice}")
