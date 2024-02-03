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


def report():
    print(resources)


def check(arg):
    if arg == "espresso":
        if MENU["espresso"]["ingredients"]["water"] <= resources["water"] and MENU["espresso"]["ingredients"]["coffee"] <= resources["coffee"]:
            resources["water"] = resources["water"] - 50
            resources["coffee"] = resources["coffee"] - 18
            return 0
        else:

            return 1
    elif arg == "latte":
        if MENU["latte"]["ingredients"]["water"] <= resources["water"] and MENU["latte"]["ingredients"]["coffee"] <= resources["coffee"] and MENU["latte"]["ingredients"]["milk"] <= resources["milk"]:
            resources["water"] = resources["water"] - 200
            resources["coffee"] = resources["coffee"] - 150
            resources["milk"] = resources["milk"] - 24
            return 0
        else:

            return 1
    elif arg == "cappuccino":
        if MENU["cappuccino"]["ingredients"]["water"] <= resources["water"] and MENU["cappuccino"]["ingredients"]["coffee"] <= resources["coffee"] and MENU["cappuccino"]["ingredients"]["milk"] <= resources["milk"]:
            resources["water"] = resources["water"] - 250
            resources["coffee"] = resources["coffee"] - 100
            resources["milk"] = resources["milk"] - 24
            return 0
        else:

            return 1


def coins(arg):
    cash = float(MENU[arg]["cost"] * 100)
    c_quarters = float(input("Enter the no of quarters\n"))
    quarters = 25 * c_quarters
    c_dimes = float(input("Enter the no of dimes\n"))
    dimes = 10 * c_dimes
    c_nickels = float(input("Enter the no of nickels\n"))
    nickels = 5 * c_nickels
    c_pennies = int(input("Enter the no of pennies\n"))
    pennies = c_pennies
    if cash < quarters + dimes + nickels + pennies:
        change = (quarters + dimes + nickels + pennies) - cash
        return change
    elif cash == quarters + dimes + nickels + pennies:
        return 0
    else:
        n_change = -1 * (quarters + dimes + nickels + pennies)
        return n_change


while True:
    prompt = input("Enter your coffee 1.espresso 2. latte 3. cappuccino ").lower()
    if prompt == "report":
        report()
        prompt = input("Enter your coffee").lower()
    elif prompt == "off":
        break
    resource = check(prompt)
    if resource == 1:
        print("Not enough resources , come again!")
        break
    coin = coins(prompt)
    coin_n = -1 * coin
    if resource == 0 and coin == 0:
        print("Enjoy your coffee")
    elif resource == 0 and coin > 0:
        print(f"Enjoy your coffee and collect your change {coin}")

    elif resource == 0 and coin < 0:
        print(f"Not enough money, collect {coin_n}\n")
