class Student:
    def __init__(self, group, admin_no, name, score=0):
        self.group = group
        self.__admin_no = admin_no
        self.__name = name
        self.__score = score

    def get_admin_no(self):
        return self.__admin_no

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_admin_no(self, admin_no):
        self.__admin_no = admin_no

    def set_name(self, name):
        self.__name = name

    def set_score(self, score):
        if score.isdigit():
            if 0 <= int(score) <= 100:
                self.__score = score
            else:
                return "Invalid input, score must be between 0 and 100 (inclusive)."
        else:
            return "Invalid input, score must be digits only."
        return True

    def show_student_info(self):
        print(f"PEM Group: {self.group}, Admin No: {self.__admin_no}, Name: {self.__name}, Score: {self.__score}")

student = None

while True:
    print("\n=== Student Management Menu ===")
    print("1. Create Student")
    print("2. Retrieve Student Info")
    print("3. Update Student Info")
    print("4. Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        group = input("Enter PEM Group: ")
        admin_no = input("Enter Admin No: ")
        name = input("Enter Name: ")
        student = Student(group, admin_no, name)
        print("Student created successfully.")
    elif choice == "2":        
        student.show_student_info()
    elif choice == "3":
        group = input("Enter new PEM Group: ")
        #student.group = group
        admin_no = input("Enter new Admin No: ")
        #student.set_admin_no(admin_no)
        name = input("Enter new Name: ")
        #student.set_name(name)
        
        while True:
            score = input("Enter new Score: ")
            val_score = student.set_score(score)
            if val_score is True:
                break
            else:
                print(val_score)

        print("Student updated successfully.")
    else:
        print("Exiting program. Goodbye!")
        break