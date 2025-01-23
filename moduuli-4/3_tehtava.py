userInput = input('Anna luku: ')

minUserNum = 0
maxUserNum = 0

while userInput != '':
    if float(userInput) < minUserNum:
        minUserNum = float(userInput)

    if float(userInput) > maxUserNum:
        maxUserNum = float(userInput)
    userInput = input('Anna luku jatkaaksesi tai tyhjä merkkijono lopettaaksesi: ')

print (f'Pienin lukusi on {minUserNum}. Suurin lukusi on {maxUserNum}.')
