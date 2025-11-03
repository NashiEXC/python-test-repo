class Student:
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name.isalpha():
            self.__name = name
            return True
        else:
            print("Name must be all alphabets.")
            return False

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
            return True
        else:
            print("Invalid score. Must be between 0 and 100")
            return False

print("===== Create Student =====")
stud_name = input("Enter Student Name: ")
stud_score = int(input("Enter Student Score: "))
stud = Student(stud_name, stud_score)
print("===== Retrieve Student Details =====")
print(f"Name: {stud.get_name()}, Score: {stud.get_score()}")
print("===== Update Student Details =====")
while True:
    upd_stud_name = input("Update Student Name: ")
    if stud.set_name(upd_stud_name):
        break

while True:
    upd_stud_score = int(input("Update Student Score: "))
    if stud.set_score(upd_stud_score):
        break

print("===== Retrieve Student Details =====")
print(f"Name: {stud.get_name()}, Score: {stud.get_score()}")
