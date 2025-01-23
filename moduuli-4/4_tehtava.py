import random

secretNumber = random.randint(1, 10)

userGuess = int(input('Ajattelin kokonaisluvun väliltä 1–10. Yritä arvata se. Anna luku: '))

while userGuess != secretNumber:
    if userGuess < secretNumber:
        print('Liian pieni arvaus')
        userGuess = int(input('Yritä uudelleen. Anna luku: '))
    else:
        print('Liian suuri arvaus')
        userGuess = int(input('Yritä uudelleen. Anna luku: '))

print('Oikein')
