MIN_LENGTH = 37
usersZanderLength = float(input('Anna kuhan pituus senttimetreinä: '))

if usersZanderLength < MIN_LENGTH:
    missingLength = MIN_LENGTH - usersZanderLength
    print(f'Kannattaa palauttaa kuha takaisin järveen. Minimipituudesta puuttuu {missingLength} cm')
