class MenuItem:
    def __init__(self, name, price, water, milk, coffee):
        self.name = name
        self.price = price
        self.ingredients = {
            'water': water,
            'milk': milk,
            'coffee': coffee
        }

class Menu:
    def __init__(self):
        self.menu = [
            MenuItem("espresso", 2.50, 200, 100, 14),
            MenuItem("latte", 2.00, 100, 50, 34),
            MenuItem("cappuccino", 3.50, 250, 30, 16)
        ]

    def get_items(self):
        return " / ".join(item.name for item in self.menu) + " / "

    def find_drink(self, drink_name):
        for item in self.menu:
            if item.name == drink_name:
                return item
        return None