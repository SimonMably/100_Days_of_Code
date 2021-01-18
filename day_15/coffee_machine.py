from machine_info import MENU, resources, coin_values, logo

print(logo)

choice = ""

quarter = coin_values["quarter"]
dime = coin_values["dime"]
nickle = coin_values["nickle"]
penny = coin_values["penny"]

current_water = resources["water"]
current_milk = resources["milk"]
current_coffee = resources["coffee"]
money_in_machine = resources["money"]


# May need to place 'money_in_machine' for the money_in_machine stuff to work
def coffee_machine():
    """The main function for the Coffee Machine. Includes main while loop etc"""
    is_turned_on = True
    global choice

    while is_turned_on:
        choice = input("\nWhat would you like? (espresso/latte/cappuccino): ")

        if choice == "off":
            is_turned_on = False
        elif choice == "report":
            print(f"Water: {current_water}ml\nMilk: {current_milk}ml\nCoffee: "
                  f"{current_coffee}g\nMoney: ${round(money_in_machine, 2)}")
        elif choice not in MENU:
            print("We're sorry, That's not on the menu. Please pick something"
                  " else")
        elif choice == "latte":
            for ingredient, amount in MENU["latte"]["ingredients"].items():
                # Checking sufficient resources for latte
                if amount > current_coffee or amount > current_milk or amount \
                        > current_water:
                    print(f"Sorry there is not enough {ingredient}")
                    return
            process_coins()
        elif choice == "espresso":
            for ingredient, amount in MENU["espresso"]["ingredients"].items():
                # Checking sufficient resources for espresso
                if amount > current_coffee or amount > current_milk or amount \
                        > current_water:
                    print(f"Sorry there is not enough {ingredient}")
                    return
            process_coins()
        elif choice == "cappuccino":
            for ingredient, amount in MENU["cappuccino"]["ingredients"].items():
                # Checking sufficient resources for cappuccino
                if amount > current_coffee or amount > current_milk or amount \
                        > current_water:
                    print(f"Sorry there is not enough {ingredient}")
                    return

            process_coins()


def deduct_resources():
    """
    If there is enough resources to make users selected beverage,
    then use values from ingredients of chosen beverage to deduct the
    required values from resources dictionary.
    """
    global choice, current_milk, current_water, current_coffee
    if choice == "espresso":
        current_water -= MENU["espresso"]["ingredients"]["water"]
        current_coffee -= MENU["espresso"]["ingredients"]["coffee"]
    elif choice == "latte":
        current_water -= MENU["latte"]["ingredients"]["water"]
        current_milk -= MENU["latte"]["ingredients"]["milk"]
        current_coffee -= MENU["latte"]["ingredients"]["coffee"]
    elif choice == "cappuccino":
        current_water -= MENU["cappuccino"]["ingredients"]["water"]
        current_milk -= MENU["cappuccino"]["ingredients"]["milk"]
        current_coffee -= MENU["cappuccino"]["ingredients"]["coffee"]


def process_coins():
    """
    Function that deals with the processing of coins. Makes sure that
    user provides correct amount of money for chosen beverage, gives user any
    change if user provides more than the required amount of money.
    """
    global choice
    total_amount = 0.0
    change = 0.0
    global money_in_machine
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        print(f"{choice.title()}'s costs "
              f"${round(MENU[choice]['cost'], 2)} each.")
        deduct_resources()

    print("\nType the amount of each coin you're entering into the machine.")
    quarter_amount = float(input("How many quarters: ")) * quarter
    dime_amount = float(input("How many dimes: ")) * dime
    nickle_amount = float(input("How many nickles: ")) * nickle
    penny_amount = float(input("How many pennies: ")) * penny
    total_amount = quarter_amount + dime_amount + nickle_amount + penny_amount

    if choice == "espresso":
        if total_amount >= MENU["espresso"]["cost"]:
            # Add cost of espresso to resources["money"]
            print(f"\nYou have entered ${round(total_amount, 2)}")
            if total_amount > MENU["espresso"]["cost"]:
                change = total_amount - MENU["espresso"]["cost"]
                print(f"Please take your £{round(change,2)} change.\nHere is "
                      f"your {choice.title()}. Enjoy!")
            total_amount = MENU["espresso"]["cost"]
            money_in_machine += total_amount
        elif total_amount < MENU["espresso"]["cost"]:
            total_amount = 0.0
            print("\nNot enough money inserted. Transaction cancelled. Your "
                  "money has been refunded.")

    elif choice == "latte":
        if total_amount >= MENU["latte"]["cost"]:
            # Add cost of espresso to resources["money"]
            print(f"\nYou have entered ${round(total_amount, 2)}")
            if total_amount > MENU["latte"]["cost"]:
                change = total_amount - MENU["latte"]["cost"]
                print(f"Please take your £{round(change, 2)} change.\nHere is "
                      f"your {choice.title()}. Enjoy!")
            total_amount = MENU["latte"]["cost"]
            money_in_machine += total_amount
        elif total_amount < MENU["latte"]["cost"]:
            total_amount = 0.0
            print("\nNot enough money inserted. Transaction cancelled. Your "
                  "money has been refunded.")

    elif choice == "cappuccino":
        if total_amount >= MENU["cappuccino"]["cost"]:
            # Add cost of espresso to resources["money"]
            print(f"\nYou have entered ${round(total_amount, 2)}")
            if total_amount > MENU["cappuccino"]["cost"]:
                change = total_amount - MENU["cappuccino"]["cost"]
                print(f"Please take your £{round(change, 2)} change.\nHere is "
                      f"your {choice.title()}. Enjoy!")
            total_amount = MENU["cappuccino"]["cost"]
            money_in_machine += total_amount
        elif total_amount < MENU["cappuccino"]["cost"]:
            total_amount = 0.0
            print("\nNot enough money inserted. Transaction cancelled. Your "
                  "money has been refunded.")


coffee_machine()
