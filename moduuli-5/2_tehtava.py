numbers_to_print = 5

user_input = input('Anna luku: ')
user_numbers = []

while user_input != "":
    user_numbers.append(float(user_input))
    user_input = input('Anna luku: ')

user_numbers.sort(reverse=True)

if len(user_numbers) < numbers_to_print:
    numbers_to_print = len(user_numbers)

for i in range(numbers_to_print):
    print(user_numbers[i])
