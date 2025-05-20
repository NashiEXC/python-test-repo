Salary = float(input("gross salary: "))
CPF = Salary /12 * 0.2
Loan = 1500
takehome = Salary/12-CPF-Loan

print(f"your monthly take home pay is {takehome:.2f}" )