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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def Money():
    quartersValue = 0.25
    dimesValue = 0.10
    nicklesValue = 0.05
    penniesValue = 0.01

    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    global dollar
    dollar=quarters * quartersValue + dimes * dimesValue + nickles * nicklesValue + penniesValue * pennies

def Resources(choice):
    if resources['water'] < MENU[choice]['ingredients']['water'] or resources['milk'] < MENU[choice]['ingredients']['milk'] or resources['coffee'] < MENU[choice]['ingredients']['coffee']:
        print("There is no enough resource. Money refund.")
        return False
    else:

        resources['water'] -= MENU[choice]['ingredients']['water']
        resources['milk'] -= MENU[choice]['ingredients']['milk']
        resources['coffee'] -= MENU[choice]['ingredients']['coffee']
        return True

def CoffeeChoice(choice, money= 0.0):
    if Resources(choice):
        if money >= MENU[choice]['cost']:
            if money - MENU[choice]['cost'] > 0:
                print(f"Here is your change {round(money-MENU[choice]['cost'],2)}")
                print(f"Here is your {choice}. Enjoy!")
        else:
            print("Sorry that's not enough money. Money refunded")
    else:
        print("Insufficient resources.")


while True:
    choice = input("What would you like? (espresso, latte, cappuccino): ")
    if choice == "report":
        print(resources)
    else:
        money = Money()
        CoffeeChoice(choice, dollar)
