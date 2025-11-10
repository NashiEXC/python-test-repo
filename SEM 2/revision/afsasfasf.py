class Smartphone:

    count = 0
    def __init__(self,brand,model):
        self.__brand = brand
        self.__model = model
        Smartphone.count += 1

   
    def set_brand(self,brand):
        self.__brand = brand
    def set_model(self,model):
        self.__model = model
    def get_phone_info(self):
        print(f"Brand: {self.__brand}, Model: {self.__model}")
        print(f"{Smartphone.count} Smartphone(s) created so far.")
        
phone= Smartphone("Apple","iPhone 17")
newmodel= input("Enter new model:")
phone.set_model(newmodel)
phone.get_phone_info()


