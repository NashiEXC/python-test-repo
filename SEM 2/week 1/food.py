class Food:
    def __init__(self, name, secret_recipe, category="Snack"):
        self.name = name
        self.category = category
        self.__secret_recipe = secret_recipe

    def show_food_info(self):
        print(f"Name: {self.name}, Category: {self.category}, Secret Recipe: {self.__secret_recipe}")

    def update_recipe(self, secret_recipe):
        self.__secret_recipe = secret_recipe

food_pizza = Food("Pizza", "Cheese Blend", "Main Dish")
food_Icecream= Food("Ice Cream", "Vanilla Extract")

food_pizza.show_food_info()
food_Icecream.show_food_info()
food_pizza.update_recipe("Tomato Sauce")
food_pizza.show_food_info()
food_Icecream.show_food_info()