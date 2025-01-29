import random

def generate_dice_roll():
    return random.randint(1, 6)

def roll_for_six():
    while True:
        res = generate_dice_roll()
        print(f'Tulos: {res}')
        if res == 6:
            break

roll_for_six()
