# code the function getValidAge


def getValidAge():
    msg = "invalid age"
    try:
        age1 = int(input("enter your age: "))
        if(age1 < 3 or age1 > 80):
            print(msg)
        else:
            return age1
    except ValueError:
        print(msg)

# code the function getTicketPrice
def getTicketPrice(age):
    if age < 21:
        return 10
    elif age < 66:
        return 30
    else:
        return 15

    
# main program calling the functions
userAge = getValidAge()
price = getTicketPrice( userAge )

print(f'Age = {userAge}, Please pay ${ price } ' )