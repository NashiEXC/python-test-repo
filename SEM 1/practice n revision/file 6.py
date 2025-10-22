results = {
'Jane': [75, 80, 85],
'John':[60, 68, 74],
'Jerome':[81, 63, 77],
'Jason':[55, 76, 67],
'Jessica':[62, 45, 68],
'Joanne':[52, 47, 51]}

name= input("Enter Student's name: ")

def result(name):
    if name in results:
        print(f"{name}'s English score is {results[name][0]}")
        print(f"{name}'s Math score is {results[name][1]}")
        print(f"{name}'s Science score is {results[name][2]}")
    else:
        print("Invalid name, please try again")

result(name)