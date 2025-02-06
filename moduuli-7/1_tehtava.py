VUODENAJAT = ('talvi', 'kevät', 'kesä', 'syksy')

users_input = int(input('Anna kuukauden numero: '))

if users_input in (12, 1, 2):
    print(VUODENAJAT[0])
elif users_input in (3, 4, 5):
    print(VUODENAJAT[1])
elif users_input in (6, 7, 8):
    print(VUODENAJAT[2])
elif users_input in (9, 10, 11):
    print(VUODENAJAT[3])
else:
    print('Tuntematon kuukauden arvo')
