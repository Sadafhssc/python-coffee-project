class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 500,
            "milk": 300,
            "coffee": 100
        }

    def report(self):
        print("Coffee Machine Report:")
        print(f"Water : {self.resources['water']} ml")
        print(f"Milk : {self.resources['milk']} ml")
        print(f"Coffee : {self.resources['coffee']} g")

    def is_resource_sufficient(self, drink):
        for item in drink.ingredients:
            if self.resources[item] < drink.ingredients[item]:
                print(f"Sorry, not enough {item}!")
                return False
        return True

    def make_coffee(self, drink):
        for item in drink.ingredients:
            self.resources[item] -= drink.ingredients[item]
        print(f"Here is your {drink.name} ☕. Enjoy!")
