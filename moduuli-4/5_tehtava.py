userId = input('Anna käyttäjätunnus: ')
userPassword = input('Anna salasana: ')

rightId = 'python'
rightPassword = 'rules'

userAttempts = 1
maxAttempts = 5

while (userId != rightId or userPassword != rightPassword) and (userAttempts < 5):
    userAttempts += 1
    userId = input('Anna käyttäjätunnus: ')
    userPassword = input('Anna salasana: ')

if userAttempts <= 5:
    print('Tervetuloa')
else:
    print('Pääsy evätty')
