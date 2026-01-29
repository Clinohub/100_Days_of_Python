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


def invalid_order():
    """
    Checks for proper order
    """
    global order
    invalid = True
    while invalid:
        if order == 'off':
            return 'Power off'
        elif not order == 'espresso' or order == 'latte' or order == 'cappuccino' or order == 'report':
            order = input("What would you like? (espresso/latte/cappuccino): ").lower()
        else:
            return order


def report(serving):
    """
    Returns ingredients of coffee ordered
    """


order = input("What would you like? (espresso/latte/cappuccino): ").lower()
invalid_order()












