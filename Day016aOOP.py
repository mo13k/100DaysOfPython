#Procedural Programming: what ive been doing so far, from up to down
#Object Oriented Programming: models virtual objects, make objects to do things, object has attributes (variables) and methods (functions), helps with big projects, blueprint for the object (ie: if i have a restaurant and want multiple waiters) is called a class (waiters in general), then the object are the instances of the class (ie: waiter 1, waiter 2, waiter 3)

#Class: blueprint, in PascalCase, first letter of each word is capitalized
#Instance: object, in camelCase, first letter of each word is lowercase
#car1 = CarBlueprint()
'''
from turtle import Turtle,Screen # using this to see objects
    timmy = Turtle()
    myscreen = Screen()
    timmy.shape("turtle")
    timmy.color("coral")
    timmy.forward(100)
    myscreen.exitonclick()
'''
'''
import prettytable # using this to see objects
    table = prettytable.PrettyTable()
    table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
    table.add_column("Type", ["Electric", "Water", "Fire"])
    table.align = "l"
    print(table)
'''

#Coffe Machine with OOP
from Day016menu import Menu
from Day016coffee_maker import CoffeeMaker
from Day016money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)
