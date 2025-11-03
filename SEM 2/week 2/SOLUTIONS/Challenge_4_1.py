class Vehicle:
    def __init__(self, brand, daily_rate):
        self.brand = brand
        self.__daily_rate = daily_rate

    def get_daily_rate(self):
        return self.__daily_rate
    
    def set_daily_rate(self, daily_rate):
        self.__daily_rate = daily_rate

    def show_info(self):
        print(f"Vehicle: {self.brand}, Daily Rate: ${self.__daily_rate:.2f}")

    def calculate_rental(self, days):
        return self.__daily_rate * days

# Child classes
class Car(Vehicle):
    def __init__(self, brand, daily_rate, luxury_rate):
        super().__init__(brand, daily_rate)
        self.__luxury_rate = luxury_rate

    def calculate_rental(self, days):
        return super().calculate_rental(days) * self.__luxury_rate

class Bus(Vehicle):
    def __init__(self, daily_rate, num_of_passengers):
        super().__init__("Mercedes", daily_rate)
        self.__num_of_passengers = num_of_passengers

    def calculate_rental(self, days):
        cost = super().calculate_rental(days)
        if self.__num_of_passengers > 30:
            cost *= 0.9  # 10% discount
        return cost

# Main program
car_brand = input("Enter car brand: ")
car_daily_rate = float(input("Enter car daily rate: "))
car_luxury_rate = float(input("Enter luxury rate: "))
car_days = int(input("Enter number of rental days for car: "))
car = Car(car_brand, car_daily_rate, car_luxury_rate)
car.show_info()
print(f"Total rental cost for 3 days: ${car.calculate_rental(car_days):.2f}")
print()
bus_daily_rate = float(input("Enter bus daily rate: "))
bus_passengers = int(input("Enter number of passengers: "))
bus_days = int(input("Enter number of rental days for bus: "))
bus = Bus(bus_daily_rate, bus_passengers)
bus.show_info()
print(f"Total rental cost for 2 days: ${bus.calculate_rental(bus_days):.2f}")
