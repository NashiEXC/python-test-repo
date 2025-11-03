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
            if 0<=int(score)<=100:
                self.__score = score
            else: 
                return "invalid input"
        else:
            return "invalid"
        return True

    def show_student_info(self):
        print(f" Group: {self.group}\n Admin: {self.__admin_no}\n Name: {self.__name}\n Score: {self.__score}")

student = None

menuruntime = 1

while menuruntime == 1:
    print("==STUDENT MANAGEMENT SYSTEM==\n1. Create\n2. Retrieve\n3. Update\n4. Quit")
    try:
        choice = int(input("Enter your choice:"))
    except ValueError:
        print("invalid, try again")
        continue

    if choice > 4:
        print("Invalid, please try again")
        continue

    if choice == 1:
        group = input("Enter PEM Group: ")
        admin = input("Enter Admin No.: ")
        name = input("Enter Name: ")
        student = Student(group, admin, name)
        print("Student Created.")
    elif choice == 2:
        student.show_student_info()
    elif choice == 3:
        group = input("Enter new PEM Group: ")
        student.group = group
        admin = input("Enter new Admin No.: ")
        student.set_admin_no(admin)
        name = input("Enter new Name: ")
        student.set_name(name)
        
        while True: 
            score = input("Enter new score")
            score_validation = student.set_score(score)
            if score_validation is True:
                break
            else:
                print(score_validation)
    else:
        print("Program ended")
        break




