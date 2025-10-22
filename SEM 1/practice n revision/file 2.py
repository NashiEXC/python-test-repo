LUamt = 5
totalCP= 0
totalCR= 0

for i in range(1, LUamt+1):
    print(f"LU {i}:")
    LUScore = float(input("Enter Score: "))
    LUCredit = float(input("Enter Credit: "))

    GPA= 0
    
    if LUScore >= 80:
        GPA = 4
    elif LUScore >= 75:
        GPA = 3.5
    elif LUScore >= 70:
        GPA = 3
    elif LUScore >= 65:
        GPA = 2.5
    elif LUScore >= 60:
        GPA = 2.0
    elif LUScore >= 55:
        GPA = 1.5
    elif LUScore >= 50:
        GPA = 1
    else:
        GPA = 0

    totalCR += LUCredit
    totalCP += LUCredit * GPA

print(f"Your GPA is {totalCP/totalCR:.2f}")
    