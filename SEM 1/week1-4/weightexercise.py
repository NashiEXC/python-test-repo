name = input("namee: ")
admin = input("Admin number")
age = input("Age: ")
gender = input("gender: ")
height = float(input("height: "))
weight = float(input("weight: "))
bmi = weight / height**2

print(f"your name is {name}, your admin number is {admin}, your age is {age}, your gender is {gender}, your height is {height}, your weight is {weight}, your bmi is", int(bmi))