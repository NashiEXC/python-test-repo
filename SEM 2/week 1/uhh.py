class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade

    def showinfo(self):
        return print(f"Student: {self.name}\nGrade: {self.__grade}")

Student_1= Student("Kristabelle", "A")
Student_2= Student("Miracast", "B")

Student_1.showinfo()