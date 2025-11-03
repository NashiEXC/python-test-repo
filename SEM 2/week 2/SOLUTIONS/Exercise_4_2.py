class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hi, my name is {self.name}.")

class Student(Person):
    def __init__(self, name, admin_no, class_name):
        super().__init__(name)
        self.admin_no = admin_no
        self.class_name = class_name

class Lecturer(Person):
    def __init__(self, name, salary, designation):
        super().__init__(name)
        self.salary = salary
        self.designation = designation

# ====== Main Program ======
# Create Student
name = input("Enter student name: ")
admin_no = input("Enter student admin number: ")
class_name = input("Enter student class: ")
student = Student(name, admin_no, class_name)

# Checking instance types
print(f"Is this student object a person? {isinstance(student, Person)}")
print(f"Is this student object a student? {isinstance(student, Student)}")
print(f"Is this student object a lecturer? {isinstance(student, Lecturer)}")

# Create Lecturer
name = input("Enter lecturer name: ")
salary = float(input("Enter lecturer salary: "))
designation = input("Enter lecturer designation: ")
lecturer = Lecturer(name, salary, designation)

# Checking instance types
print(f"Is this lecturer object a person? {isinstance(lecturer, Person)}")
print(f"Is this lecturer object a student? {isinstance(lecturer, Student)}")
print(f"Is this lecturer object a lecturer? {isinstance(lecturer, Lecturer)}")
