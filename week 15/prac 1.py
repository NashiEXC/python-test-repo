def SGD_convert( Currency, Amt, pDict ):
    # can find this key means valid currency
    if(Currency in pDict):
        returnAmt = Amt * pDict[Currency]
        return (returnAmt)
    else:
        # return -1 to mean invalid currency
        returnAmt = -1
        return (returnAmt)
    
to = input('Currency to convert: ')
to = to.upper() #convert all alpha input into uppercase
original = float(input('SGD amount to convert : '))

convertDict = {"USD":0.73,"EUR":0.63}
amount = SGD_convert(to, original,convertDict)

if( amount == -1):
    print(f'Sorry, {to} is currently not supported')
else:
    print(f"{original} SGD converts to {amount} {to}")