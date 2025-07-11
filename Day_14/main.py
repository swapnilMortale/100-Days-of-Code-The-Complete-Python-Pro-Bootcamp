# Coffee Machine Simulation in Python

MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

def print_report():
    """Prints current machine resource status."""
    print(f"\n🔧 Machine Report:")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}\n")

def is_resource_sufficient(order_ingredients):
    """Checks if resources are sufficient to make the drink."""
    for item in order_ingredients:
        if resources.get(item, 0) < order_ingredients[item]:
            print(f"❌ Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    """Processes inserted coins and returns total amount."""
    print("💰 Please insert coins:")
    quarters = int(input("  Quarters ($0.25): ")) * 0.25
    dimes = int(input("  Dimes ($0.10): ")) * 0.10
    nickels = int(input("  Nickels ($0.05): ")) * 0.05
    pennies = int(input("  Pennies ($0.01): ")) * 0.01
    total = round(quarters + dimes + nickels + pennies, 2)
    print(f"🧾 Total inserted: ${total}")
    return total

def handle_transaction(payment, cost):
    """Validates the transaction and handles change."""
    if payment < cost:
        print("❌ Not enough money. Money refunded.")
        return False
    change = round(payment - cost, 2)
    if change > 0:
        print(f"💸 Here is your change: ${change}")
    resources["money"] += cost
    return True

def make_coffee(drink_name, ingredients):
    """Deducts resources and 'makes' the coffee."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"☕ Here is your {drink_name}. Enjoy!\n")

def coffee_machine():
    """Main function to run the coffee machine."""
    print("🚀 Welcome to the Coffee Machine!\n")
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino/report/off): ").lower()

        if choice == "off":
            print("🛑 Turning off the coffee machine. Goodbye!")
            break

        elif choice == "report":
            print_report()

        elif choice in MENU:
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                payment = process_coins()
                if handle_transaction(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
        else:
            print("⚠️ Invalid input. Please choose again.\n")

# Run the machine
coffee_machine()
