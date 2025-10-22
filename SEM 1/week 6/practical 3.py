price=float(input("enter a number:"))

while (price>=0):
    if price ==0:
        break
    print(price*1.25)
    price=float(input("enter a number:"))  
else: 
    print ("only numerical values")
    price=float(input("enter a number:"))  
print("program end")