def filter_for_even(numbers_list):
    filtered_list = numbers_list[:]
    for num in numbers_list:
        if (num % 2) != 0:
            filtered_list.remove(num)
    return filtered_list

def test_filter_for_even():
    numbers_list = [-2, -1, 0, 1, 2, 3, 4, 5, 6]
    print(f'Alkuperäinen lista: {numbers_list}')
    print(f'Karsitun lista: {filter_for_even(numbers_list)}')

test_filter_for_even()