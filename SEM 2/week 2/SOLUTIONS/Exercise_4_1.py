# Parent class
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
        return f"Brand: {self.brand}, Max Speed: {self.max_speed}km/h, Fuel Type: {self.__fuel_type}"
    
    def start(self):
        print("Vehicle started...")

# Child classes
class Truck(Vehicle):
    def load_cargo(self):
        print("Loading cargo onto truck...")

class Bus(Vehicle):
    def announce_stop(self):
        print("Bus is stopping!")


# Main program
truck_brand = input("Enter truck brand: ")
truck_speed = input("Enter truck max speed: ")
truck_fuel_type = input("Enter truck fuel type: ")
truck = Truck(truck_brand, truck_speed, truck_fuel_type)
truck.start()
print(truck.show_info())
truck.load_cargo()
print()
bus_brand = input("Enter bus brand: ")
bus_speed = input("Enter bus max speed: ")
bus_fuel_type = input("Enter bus fuel type: ")
bus = Bus(bus_brand, bus_speed, bus_fuel_type)
bus.start()
print(bus.show_info())
bus.announce_stop()
