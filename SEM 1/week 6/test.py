cost = float(input("Cost? "))
while cost>=0:
    try:
        if cost ==0:
            break
        if cost <=0:
            print("postive only")
            continue
        print(cost*1.25)
        cost = float(input("Cost? "))
    except:
        print("only numerical value")
        cost = float(input("Cost? "))
print("programm end")