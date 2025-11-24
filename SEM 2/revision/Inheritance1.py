class Vehicle:
    def __init__(self, brand, max_speed, fuel_type):
        self.brand = brand
        self.max_speed = max_speed
        self.__fuel_type = fuel_type

    def get_fuel_type(self):
        return self.__fuel_type
    def set_fuel_type(self, fuel_type):
        self.__fuel_type = fuel_type
    def show_info(self):
        print(f"Brand: {self.brand}\nMax Speed: {self.max_speed}\nFuel Type: {self.__fuel_type}")
    def start(self):
        print("Vehicle Started")

class Truck(Vehicle):
    def load_cargo(self):
        print("Loading cargo...")

class Bus(Vehicle):
    def announce_stop(self):
        print("Bus stopped")


#truck
brand = input("Enter Brand: ")
speed = input("Enter Max Speed")
fuel = input("Enter Fuel Type: ")

t = Truck(brand, speed, fuel)
t.show_info()
t.start()
t.load_cargo()

#bussy
brand = input("Enter Brand: ")
speed = input("Enter Max Speed")
fuel = input("Enter Fuel Type: ")
b = Bus(brand, speed, fuel)
b.show_info
b.start()
b.announce_stop()

