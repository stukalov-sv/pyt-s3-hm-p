# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

def random_int_fill_list(size: int) -> list:
    result_list = []
    for i in range(size):
        result_list.append(random.randrange(-10, 11))
    return result_list

def pair_numbers_multiply(user_list: list) -> list:
    result_list_multiply = []
    for i in range(len(user_list) // 2):
        result_list_multiply.append(user_list[i] * user_list[-1 - i])
    if (len(user_list) % 2 != 0):
        result_list_multiply.append(user_list[len(user_list) // 2] ** 2)
    return result_list_multiply

random_list = random_int_fill_list(int(input('Enter list length: ')))
print(f'Random list:\n{random_list}')

result_multiply = pair_numbers_multiply(random_list)

print(f'Multiply numbers list: {result_multiply}')
