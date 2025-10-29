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
                print("invalid input")
        else:
            print("invalid")

    def show_student_info(self):
        print(f" Group: {self.group}\n Admin: {self.__admin_no}\n Name: {self.__name}\n Score: {self.__score}")

student = None

menuruntime = 1

while menuruntime == 1:
    pass