#string slicing ^q^
def summation(low, high):
    result = 0
    for i in range(low, high+1):
        result += i
    return result

print(summation(1,10))