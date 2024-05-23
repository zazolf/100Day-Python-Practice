from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
menu_object = Menu()
coffeemaker_object = CoffeeMaker()
moneymachine_object = MoneyMachine()

make_coffee = True
while make_coffee:
    options = menu_object.get_items()
    order_name = input(f"What would you like?:  ({options:})")
    
   

    if order_name == "report":
        print(coffeemaker_object.report())
        print(moneymachine_object.report())
    elif order_name == "off":
        make_coffee = False
    else:
        menu_item = menu_object.find_drink(order_name)
        if coffeemaker_object.is_resource_sufficient(menu_item):
            if moneymachine_object.make_payment(menu_item.cost):
                coffeemaker_object.make_coffee(menu_item)
    
    

   



    
    
    
    

    