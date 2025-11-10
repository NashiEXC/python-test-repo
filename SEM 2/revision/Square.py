import Shape as Shape

class Square(Shape):
    def __init__(self, side, length):
        super().__init__(side)
        self.length = length

    def calculate_perimeter(self):
        return self.get_side() * self.length
    
    def show_square_info(self):
        print(f"Square with {self.get_side()} side and length of {self.length} has a perimeter of {self.calculate_perimeter()}")


