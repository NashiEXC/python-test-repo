age = int(input("Enter age:"))


if age >= 4:
    day = int(input("enter day of the week (1-7)"))
    if day >= 6:
        print("$9.00")
    elif age <= 16 :
        print("7.50")
    elif age >= 16 and age < 65:
        print("$10.00")
    elif age  :
else:
    print("age invalid")