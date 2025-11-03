class Product:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def show_info(self):
        print(f"Product: {self.__name}, Price: ${self.__price:.2f}")

class TV(Product):
    def __init__(self, name, price, screen_size):
        super().__init__(name, price)
        self.__screen_size = screen_size

    def get_screen_size(self):
        return self.__screen_size

    def show_info(self):
        print(f"TV: {self.get_name()}, Price: ${self.get_price():.2f}, Screen Size: {self.__screen_size} inches")

class Laptop(Product):
    def __init__(self, name, price, ram_size):
        super().__init__(name, price)
        self.__ram_size = ram_size

    def get_ram_size(self):
        return self.__ram_size

    def show_info(self):
        print(f"Laptop: {self.get_name()}, Price: ${self.get_price():.2f}, RAM Size: {self.__ram_size}GB")

# ===== Main Program =====
tv_list = []
laptop_list = []

print("=== Product Entry System ===")
print("Type 'Q' anytime to stop adding products.\n")

while True:
    name = input("Enter product name (or 'Q' to quit): ")
    if name == "Q":
        print("Exiting product entry...\n")
        break
    
    price = float(input("Enter product price: "))
    product_type = input("Enter product type (TV/Laptop): ")

    if product_type == "TV":
        screen_size = input("Enter screen size: ")
        product = TV(name, price, screen_size)
    else:
        ram_size = input("Enter RAM size (GB): ")
        product = Laptop(name, price, ram_size)

    while True:
        store_choice = input("Do you want to store this in (TV/Laptop) list? ")
        
        if store_choice == "TV":
            if isinstance(product, TV):
                tv_list.append(product)
                print("Product stored in TV list!\n")
                break
            else:
                print("Cannot store a Laptop object in the TV list!")

        elif store_choice == "Laptop":
            if isinstance(product, Laptop):
                laptop_list.append(product)
                print("Product stored in Laptop list!\n")
                break
            else:
                print("Cannot store a TV object in the Laptop list!")

print("--- TV List ---")
if tv_list:
    for tv in tv_list:
        tv.show_info()
print("\n--- Laptop List ---")
if laptop_list:
    for laptop in laptop_list:
        laptop.show_info()
