import random

dotsCounter = int(input('Anna pisteiden määrä: '))
dotsInCircleCounter = 0
startCounter = 0

while startCounter < dotsCounter:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    isDotInCircle = ((x**2) + (y**2)) < 1

    if isDotInCircle:
        dotsInCircleCounter += 1

    startCounter += 1

pi = 4 * (dotsInCircleCounter / dotsCounter)

print(f'π:n likiarvo: {pi}')
