def sum_numbers(numbers_list):
    summa = 0
    for num in numbers_list:
        summa += num
    return summa

def test_sum_numbers():
    numbers = [1, 2, 3, 4, 5]
    print(sum_numbers(numbers))

test_sum_numbers()
