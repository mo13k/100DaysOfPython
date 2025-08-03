#Requirements:
#Espresso: 50ml water, 18g coffee, $1.50
#Latte: 200ml water, 24g coffee, 150ml milk, $2.50
#Cappuccino: 250ml water, 24g coffee, 100ml milk, $3.00

#Resources:
#Water: 300ml
#Milk: 200ml
#Coffee: 100g

#Coin Operated: Penny, Nickel, Dime, Quarter - 0.01, 0.05, 0.10, 0.25
#Must be able to print report of all resources and money
#Check if resources are sufficient
#Process Coins - ask to insert each type of coin and calculate change required or refund if not
#Make Coffee - deduct resources

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": { 
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 100,
}

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickels": 0.05,
    "pennies": 0.01,
}

profit = 0

#TODO: Create Report to show all resources
#TODO: Check if resources are sufficient
#TODO Process Coins
#TODO: Check if transaction is successful
#TODO: Make Coffee (deduct resources)
#TODO: Check Profits and Set off as end word

def report(resources):
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")

def is_resource_sufficient(drink):
    for item in drink["ingredients"]:
        if resources[item] < drink["ingredients"][item]:
            print(f"Sorry there is not enough {item}. Please restock.")
            return False
    return True

def istransactionsuccessful(totalpayment, price):
    if totalpayment >= price:
        change = totalpayment - price
        print(f"Here is ${change} in change.")
        global profit
        profit += price
        makecoffee(order, drink["ingredients"], resources)
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def makecoffee(order, ingredients, resources):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {order} ☕️. Enjoy!")
ison = True
while ison:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        print("Machine is off.")
        ison = False
    elif order == "report":
        report(resources)
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        drink = menu[order]
        if is_resource_sufficient(drink):
            price = menu[order]["cost"]
            print("Please insert coins.")
            totalpayment = sum(int(input(f"How many {coin}? ")) * coins[coin] for coin in coins)
            istransactionsuccessful(totalpayment, price)
        else:
            ison = False
    else:
        print("Invalid input. Please try again.")
        
    