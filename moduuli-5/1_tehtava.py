import random

dices = int(input('Anna arpakuutioiden lukumäärä: '))
total_score = 0

for dice in range(dices):
    total_score += random.randint(1, 6)

print(f'Silmälukujen summa: {total_score}')
