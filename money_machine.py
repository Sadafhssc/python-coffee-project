class MoneyMachine:
    def __init__(self):
        self.coins = {
            "penny": 0.01,
            "dime": 0.10,
            "nickel": 0.25,
            "quarter": 0.50
        }
        self.money = 0

    def report(self):
        print(f"Money: ${self.money:.2f}")

    def perform_transaction(self, price):
        print("Insert Coins:")
        try:
            penny = int(input("Penny: "))
            dime = int(input("Dime: "))
            nickel = int(input("Nickel: "))
            quarter = int(input("Quarter: "))
        except ValueError:
            print("Invalid input. Transaction cancelled.")
            return False

        total = (
            penny * self.coins["penny"] +
            dime * self.coins["dime"] +
            nickel * self.coins["nickel"] +
            quarter * self.coins["quarter"]
        )

        if total < price:
            print("Sorry! You don't have enough money! Refunding.")
            return False
        else:
            change = round(total - price, 2)
            if change > 0:
                print(f"Transaction successful! Change: ${change:.2f}")
            else:
                print("Transaction successful! No change.")
            self.money += price
            return True
