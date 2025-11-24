class Person:
    def __init__(self, name):
        self.name = name
    def introduce(self):
        print(f"This is {self.name}")
    
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

stuname = input("Enter student name: ")
admin = input("Enter admin: ")
studentclass = input("Enter class:")
stu= Student(stuname, admin, studentclass)
print(f"Is this object a person: {isinstance(stu, Person)}")
print(f"Is this object a student: {isinstance(stu, Student)}")
print(f"Is this object a lecturerw: {isinstance(stu, Lecturer)}")
lecname = input("Enter lecturer name: ")
salary = input("Enter salary: ")
desig = input("Enter designation: ")
lec= Lecturer(lecname, salary, desig)
print(f"Is this object a person: {isinstance(lec, Person)}")
print(f"Is this object a student: {isinstance(lec, Student)}")
print(f"Is this object a lecturerw: {isinstance(lec, Lecturer)}")
