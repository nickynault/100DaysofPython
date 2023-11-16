from coffee_data import MENU as menu
from coffee_data import resources as report
from math import ceil
import time


def pay(price, q, d, n, p):
    total = (q * 0.25) + (d * 0.10) + (n * 0.05) + (p * 0.01)
    change = ceil((total - price) * 100) / 100
    if total >= price:
        print(f"Thanks! Your change is: ${change}")
        return True
    else:
        return False


def generate_report():
    print("Current Resources:")
    for resource, quantity in report.items():
        print(f"{resource}: {quantity}")
    print("")


def check_resources(x):
    coffee = menu[x]
    required = coffee.get("ingredients", {})
    for resource, quantity in required.items():
        if quantity > report.get(resource, 0):
            return False
    return True


def alter_resources(x):
    coffee = menu[x]
    required = coffee.get("ingredients", {})
    for resource, quantity in required.items():
        report[resource] -= quantity


def coffee_machine():
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == 'report':
        print("Generating report...\n")
        time.sleep(1)
        generate_report()
        coffee_machine()
    elif choice == 'off':
        print("Turning off the coffee machine! Bye!")
        exit()

    coffee = menu[choice]
    cost = coffee["cost"]

    if check_resources(choice):
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))

        if pay(cost, quarters, dimes, nickels, pennies) and check_resources(choice):
            print(f"\nHere is your {choice}☕️. Enjoy!\n")
            alter_resources(choice)
            coffee_machine()
        else:
            print("\nSorry, that's not enough money. Money refunded.\n")
            coffee_machine()
    else:
        print("\nSorry, there are not enough resources to make your drink. Maybe pick something else?\n")
        coffee_machine()


coffee_machine()
