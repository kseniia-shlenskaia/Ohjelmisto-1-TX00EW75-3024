userYear = int(input('Anna vuosi: '))
isLeapYear = (userYear % 4 == 0 and userYear % 100 != 0) or (userYear % 100 == 0 and userYear % 400 == 0)

if isLeapYear:
    print('Annettu vuosi on karkausvuosi')
else:
    print('Annettu vuosi ei ole karkausvuosi')
