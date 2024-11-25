from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffeemaker=CoffeeMaker()
monetary=MoneyMachine()
menu=Menu()

is_on=True


while is_on:
    options=menu.get_items()
    choice=input(f"What would you like? ({options})")
    if choice=="off":
        is_on=False
    elif choice=="report":
        my_coffeemaker.report()
        monetary.report()    
    else:
        drink=menu.find_drink(choice)
        if my_coffeemaker.is_resource_sufficient(drink):
            if monetary.make_payment(drink.cost):
                my_coffeemaker.make_coffee(drink)
