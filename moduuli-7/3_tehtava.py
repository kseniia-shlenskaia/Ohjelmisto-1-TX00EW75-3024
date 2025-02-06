airports = {}

while True:
    print('Valitse toiminto:')
    print('1 – Syöttää uuden lentoaseman')
    print('2 – Hakea syötetyn lentoaseman tiedot')
    print('3 – Lopettaa')

    users_input = input('Valintasi: ')

    if users_input == '1':
        koodi = input('Anna lentoaseman ICAO-koodi: ')
        nimi = input('Anna lentoaseman nimi: ')
        if koodi and nimi:
            airports[koodi.upper()] = nimi
            print('Lentoaseman tiedot tallennettu\n')
        else:
            print('Virheelliset tiedot')
    elif users_input == '2':
        koodi = input('Anna lentoaseman ICAO-koodi: ').upper()
        if koodi in airports:
            print(f'Haettu lentoasema: {airports[koodi]}\n')
        else:
            print('Lentoasemaa ei löydy\n')
    elif users_input == '3':
        break
    else:
        print('Tuntematon arvo\n')
        print()
