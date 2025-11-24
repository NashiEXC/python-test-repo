class Vehicle:
    def __init__(self,brand, fuel_type, capacity):
        self.__brand = brand
        self.__fuel_type = fuel_type
        self.__capacity = capacity

    def get_brand(self):
        return self.__brand
    def start_engine(self):
        print(f"Vehicle engine msg test {self.__brand}")
    def calculate_cost(distance):
        return int(distance) * 2
    def display_info(self):
        print(f"Brand: {self.__brand}, Fuel type: {self.__fuel_type}, Capacity: {self.__capacity},")

class Truck(Vehicle):
    def __init__(self,brand, fuel_type, capacity, load_limit, maintenance_rate):
        super().__init__(brand, fuel_type, capacity)
        self.__load_limit = load_limit
        self.__maintenance_rate = maintenance_rate
    def start_engine(self):
        print(f"Truck engine test msg {self.get_brand()}")
    def calculate_cost(self, distance):
        return int(distance) * float(self.__maintenance_rate)
    def display_info(self):
        super().display_info() 
        print(f"Load Limit: {self.__load_limit} tons, Maintenance Rate: {self.__maintenance_rate}")

class Bus(Vehicle):
    def __init__(self, brand, fuel_type, capacity, num_passengers, ticket_price):
        super().__init__(brand, fuel_type, capacity)
        self.__num_passengers = num_passengers
        self.__ticket_price = ticket_price
    def start_engine(self):
        print(f"Bus engine test msg {self.get_brand()}")
    def calculate_cost(self, distance):
        return int(distance) * 1.5 + int(self.__num_passengers) * float(self.__ticket_price)
    def display_info(self):
        super().display_info()
        print(f"Passengers: {self.__num_passengers}, Ticket Price: ${self.__ticket_price}")

t= Truck("Volvo", "Diesel", "2", "50", "3.5")
b= Bus("Mercedes", "Diesel", "50", "40", "2.50")
tdist = 120
bdist = 120
print("Fleet Info:")
t.display_info()
b.display_info()
print("Starting Engines:")
t.start_engine()
b.start_engine()
print("Calculating Costs:")
print(f"Truck Cost for {tdist}km: {t.calculate_cost(tdist):.2f}")
print(f"Bus Cost for {bdist}km: {b.calculate_cost(bdist):.2f}")