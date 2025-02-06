nimet = set()

while True:
    user_input = input('Anna nimi: ')

    if user_input == '':
        break

    if user_input in nimet:
        print('Aiemmin syötetty nimi')
    else:
        print('Uusi nimi')
        nimet.add(user_input)

for nimi in nimet:
    print(nimi)
