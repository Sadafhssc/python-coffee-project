# from menu import Menu
# from coffee_maker import CoffeeMaker
# from money_machine import MoneyMachine
#
# menu = Menu()
# coffee_maker = CoffeeMaker()
# money_machine = MoneyMachine()
#
# is_turn = "on"
#
# while is_turn == "on":
#     options = menu.get_items()
#     choice = input(f"Choose an option ({options}report/off): ").lower()
#
#     if choice == "off":
#         is_turn = "off"
#     elif choice == "report":
#         coffee_maker.report()
#         money_machine.report()
#     else:
#         drink = menu.find_drink(choice)
#         if drink:
#             if coffee_maker.is_resource_sufficient(drink) and money_machine.perform_transaction(drink.price):
#                 coffee_maker.make_coffee(drink)
#         else:
#             print("Sorry, that drink is not available.")
