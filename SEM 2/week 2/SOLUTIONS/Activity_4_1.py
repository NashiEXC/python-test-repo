# Base class Animal
class Animal:
    def __init__(self, name, weight, color, age):
        self.name = name
        self.weight = weight
        self.color = color
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

# Derived class Bird
class Bird(Animal):
    def __init__(self, name, weight, color, age, wing_span):
        Animal.__init__(self, name, weight, color, age)
        self.wing_span = wing_span
# Derived class Fish
class Fish(Animal):
    def __init__(self, name, weight, color, age, fin_count, water_type):
        super().__init__(name, weight, color, age)
        self.fin_count = fin_count
        self.water_type = water_type

# Create a Bird object
parrot = Bird("Polly", 1.2, "green", 2, 25)
print("Bird Details:")
print(f"Name: {parrot.name}")
print(f"Weight: {parrot.weight} kg")
print(f"Color: {parrot.color}")
print(f"Age: {parrot.get_age()} years")
print(f"Wing Span: {parrot.wing_span} cm")

# Create a Fish object
goldfish = Fish("Goldie", 0.3, "gold", 1, 6, "freshwater")
print("Fish Details:")
print(f"Name: {goldfish.name}")
print(f"Weight: {goldfish.weight} kg")
print(f"Color: {goldfish.color}")
print(f"Age: {goldfish.get_age()} years")
print(f"Fin Count: {goldfish.fin_count}")
print(f"Water Type: {goldfish.water_type}")
