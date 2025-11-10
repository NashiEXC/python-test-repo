class Shape:
    def __init__(self,side):
        self.__side = side
        
    def get_side(self):
        return self.__side
    def calculate_perimeter(self):
        return 0