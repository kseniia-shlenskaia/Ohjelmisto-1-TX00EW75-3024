import math

def get_pizza_unit_price(diameter_sm, price):
    radius_m = (diameter_sm / 100) / 2
    area = math.pi * (radius_m ** 2)

    price_per_square_m = price / area
    return price_per_square_m

def get_better_pizza():
    better_pizza = ''

    first_diameter_cm = float(input('Anna ensimmäisen pizzan halkaisija senttimetreinä: '))
    first_price = float(input('Anna ensimmäisen pizzan hinta: '))
    second_diameter_cm = float(input('Anna toisen pizzan halkaisija senttimetreinä: '))
    second_price = float(input('Anna toisen pizzan hinta: '))

    first_unit_price = get_pizza_unit_price(first_diameter_cm, first_price)
    second_unit_price = get_pizza_unit_price(second_diameter_cm, second_price)

    if first_unit_price < second_unit_price:
        better_pizza = 'ensimmäinen'
    elif first_unit_price > second_unit_price:
        better_pizza = 'toinen'
    else:
        better_pizza = 'molemmat'

    print(f'Parhaimman vastineen antava pizza: {better_pizza}.')

get_better_pizza()