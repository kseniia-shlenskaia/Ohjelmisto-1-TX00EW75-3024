import random

kolmNumKoodi = f"{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"
nelNumKoodiFirstInt = f"{random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}{random.randint(1, 6)}"

print(f'Kolmenumeroisen koodi: {kolmNumKoodi}, nelinumeroisen koodi: {nelNumKoodiFirstInt}')
