from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


class Main:
    """Main class that utilises other classes to model an actual coffee
    machine."""

    def __init__(self):
        self.money_machine = MoneyMachine()
        self.coffee_maker = CoffeeMaker()
        self.menu = Menu()

    def coffee_machine(self):
        """Main method for whole Coffee Machine program."""
        self.menu = Menu()
        self.coffee_maker = CoffeeMaker()
        self.money_machine = MoneyMachine()

        is_on = True

        while is_on:
            beverages = self.menu.get_items()
            choice = input(f"\nWhat would you like? {beverages}: ").lower()
            if choice == "off":
                is_on = False
            elif choice == "report":
                self.coffee_maker.report()
                self.money_machine.report()
            elif choice:
                coffee = self.menu.find_drink(choice)
                if coffee and self.coffee_maker.is_resource_sufficient(coffee):
                    if self.money_machine.make_payment(coffee.cost):
                        self.coffee_maker.make_coffee(coffee)


Main().coffee_machine()
