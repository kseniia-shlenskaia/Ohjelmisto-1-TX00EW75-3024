user_number = int(input('Anna kokonaisluku: '))
is_divisible = False

for num in range(2, user_number):
    if not (user_number % num):
        is_divisible = True

if is_divisible:
    print(f'{user_number} ei ole alkuluku')
else:
    print(f'{user_number} on alkuluku')
