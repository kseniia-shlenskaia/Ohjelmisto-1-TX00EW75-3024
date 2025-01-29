import random

total_face_count = int(input('Anna nopan tahkojen yhteismäärä: '))

def generate_dice_roll(max_value):
    return random.randint(1, max_value)

def roll_for_total(total_rolls_value):
    while True:
        res = generate_dice_roll(total_rolls_value)
        print(f'Tulos: {res}')
        if res == total_rolls_value:
            break

roll_for_total(total_face_count)
