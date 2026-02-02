# Coffee Machine
# 100 Days of Code ! Day 15

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


water = 300
milk = 200
coffee = 100
money = 0


def ingredients(order, water, milk, coffee):
    """
    Checks if availability of remaining ingredients
    """
    if water < MENU[order]['ingredients']['water']:
        return 'water'
    if order in {'latte', 'cappuccino'} and milk < MENU[order]['ingredients']['milk']:
        return 'milk'
    if coffee < MENU[order]['ingredients']['coffee']:
        return 'coffee'
    return None


def main(water,milk,coffee,money):
    power_on = True
    while power_on:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if not order in {'espresso', 'latte', 'cappuccino', 'report', 'off'}:
            print("Invalid choice,please try again.")
        elif order == 'report':
            print(f"Water: {water}ml")
            print(f"Milk: {milk}ml")
            print(f"Coffee: {coffee}g")
            print(f"Money: ${money}")
        else:
            power_on = False

    if order == 'off':
        print("Power off")
        return

    remaining_ing = ingredients(order, water, milk, coffee)
    if remaining_ing in {'water', 'milk', 'coffee'}:
        print(f"Sorry, there is not enough {remaining_ing}.")
        main(water,milk,coffee,money)
        return

    print("Please insert coins.")
    amt = []
    denominations = ['quarters', 'dimes', 'nickels', 'pennies']
    for denomination in denominations:
        amt.append(int(input(f"How many {denomination}?: ")))

    total_amt = amt[0]*0.25 + amt[1]*0.10 + amt[2]*0.05 + amt[3]*0.01

    if total_amt < MENU[order]['cost']:
        print("Sorry, that's not enough money. Money refunded.")
        main(water,milk,coffee,money)
        return
    
    water -= MENU[order]['ingredients']['water']
    if order in {'latte', 'cappuccino'}:
        milk -= MENU[order]['ingredients']['milk']
    coffee -= MENU[order]['ingredients']['coffee']

    money += round(MENU[order]['cost'], 2)
    change = round((total_amt - MENU[order]['cost']), 2)

    print(f"Here is your ${change} in change.")
    print(f"Here is your {order}. Enjoy!")

    main(water,milk,coffee,money)

main(water,milk,coffee,money)
