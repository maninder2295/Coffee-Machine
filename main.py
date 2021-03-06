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
quater = 0.25
dime = 0.10
nickel = 0.05
penny = 0.01


def calculate_monney(x_quater, x_dime, x_nickel, x_penny):
    total = (quater * x_quater) + (dime * x_dime) + (nickel * x_nickel) + (penny * x_penny)
    return total


def money_cal(coffee_cost, x):
    coffee_flavor = ['espresso', 'latte', 'cappuccino']
    x_quater = float(input("how many quaters?: "))
    x_dime = float(input("how many dime?: "))
    x_nickel = float(input("how many nickel?: "))
    x_penny = float(input("how many penny?: "))
    answer = round(calculate_monney(x_quater, x_dime, x_nickel, x_penny), 2)
    if answer < coffee_cost:
        return f"It's ${answer}.You can't buy Coffee with this. "
        exit()

    elif answer == coffee_cost and x in coffee_flavor:
        return answer

    elif answer > coffee_cost and x in coffee_flavor:
        total_answer = answer - coffee_cost
        return f'Here is ${total_answer} in change'


# money(2.5,'latte')


def resource():
    water = 300
    milk = 200
    coffee = 100
    return [water, milk, coffee]


def latte(items):
    water = 200
    milk = 150
    coffee = 24
    cost = 2.5
    if items == 'ingredients':
        return [water, milk, coffee]
    elif items == 'cost':
        return cost


def espresso(items):
    water = 50
    milk = 0
    coffee = 18
    cost = 1.5
    if items == 'ingredients':
        return [water, milk, coffee]
    elif items == 'cost':
        return cost


def cappuccino(items):
    water = 250
    milk = 100
    coffee = 24
    cost = 3.0
    if items == 'ingredients':
        return [water, milk, coffee]
    elif items == 'cost':
        return cost


# def select_flavour(flavour,ingidents,cost):
#     water = 0
#     milk = 0
#     coffee = 0
#     cost = 0
#     for element in Menu:
#         if item == element:


# money(cappuccino('cost'),'cappuccino')
# def is_resource_sufficient():
def subtractor(x_list, y_list):
    answer = []
    x_y = zip(x_list, y_list)
    for x1, y1 in x_y:
        answer.append(x1 - y1)
    return answer


def choice(user):
    if user == 'espresso':
        total_resources = subtractor(resource(), espresso('ingredients'))
        return total_resources
    elif user == 'latte':
        total_resources = subtractor(resource(), latte('ingredients'))
        return total_resources
    elif user == 'cappuccino':
        total_resources = subtractor(resource(), latte('ingredients'))
        return total_resources


def machine_on():
    money = 0
    espresso = 1.5
    latte = 2.5
    cappuccino = 3.0
    resources_end = False
    remaining_water = 300
    remaining_milk = 200
    remaining_coffee = 100

    while not resources_end:
        user = input("What would you like? (espresso/latte/cappuccino): ")
        print('Please insert coins')

        if user == 'espresso':
            if remaining_water <= 49:
                resources_end = True
                print(f"Sorry out of water.Remaining water is {remaining_water}ml")
            elif remaining_coffee <= 17:
                resources_end = True
                print(f"Sorry out of coffee.Remaining coffee is {remaining_coffee}ml")
            else:
                money += espresso
                print(money_cal(1.5, user))

                remaining_water -= 50
                remaining_coffee -= 18


        elif user == 'latte':
            if remaining_water <= 199:
                resources_end = True
                print(f"Sorry out of water.Remaining water is {remaining_water}ml")
            elif remaining_coffee <= 23:
                resources_end = True
                print(f"Sorry out of coffee.Remaining coffee is {remaining_coffee}ml")
            else:
                money += latte
                print(money_cal(2.5, user))

                remaining_water -= 200
                remaining_milk -= 150
                remaining_coffee -= 24


        elif user == 'cappuccino':
            if remaining_water <= 249:
                resources_end = True
                print(f"Sorry out of water.Remaining water is {remaining_water}ml")
            elif remaining_coffee <= 23:
                resources_end = True
                print(f"Sorry out of coffee.Remaining coffee is {remaining_coffee}ml")
            else:
                money += cappuccino
                print(money_cal(3, user))

                remaining_water -= 250
                remaining_milk -= 100
                remaining_coffee -= 24

        if user == 'report':
            print(
                f"Remaining resources left\nwater = {remaining_water}\nmilk = {remaining_milk}\ncoffee = {remaining_coffee}")
            print(f"Total money is ${money}")


machine_on()
