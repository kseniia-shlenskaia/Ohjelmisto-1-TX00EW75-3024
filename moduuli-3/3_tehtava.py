femaleHbMinLevel = 117
femaleHbMaxLevel = 175
maleHbMinLevel = 134
maleHbMaxLevel = 195

userGender = input('Anna biologinen sukupuolesi kirjaimella N (naisille) tai M (miehille): ').upper()

if userGender not in ('M', 'N'):
    print('Ohjelmalle tuntematon input')
    exit()

userHbLevel = float(input('Anna hemoglobiiniarvosi numeroina: '))

if userGender == 'N':
    if userHbLevel < femaleHbMinLevel:
        print('Hemoglobiiniarvosi on alhainen')
    elif userHbLevel > femaleHbMaxLevel:
        print('Hemoglobiiniarvosi on korkea')
    else:
        print('Hemoglobiiniarvosi on normaali')
else:
    if userHbLevel < maleHbMinLevel:
        print('Hemoglobiiniarvosi on alhainen')
    elif userHbLevel > maleHbMaxLevel:
        print('Hemoglobiiniarvosi on korkea')
    else:
        print('Hemoglobiiniarvosi on normaali')
