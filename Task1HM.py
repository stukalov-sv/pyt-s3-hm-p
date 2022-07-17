# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

def random_int_fill_list(size: int) -> list:
    result_list = []
    for i in range(size):
        result_list.append(random.randrange(-10, 11))
    return result_list

def odd_list_indexes_amount(user_list: list) -> int:
    result_amount = 0
    for i in range(len(user_list)):
        if (i % 2 != 0):
            result_amount += user_list[i]
            print(user_list[i])
    return result_amount

random_list = random_int_fill_list(int(input('Enter list length: ')))
print(f'Random list:\n{random_list}')

print('Odd indexes numbers:')
result_amount = odd_list_indexes_amount(random_list)

print(f'Odd indexes numbers amount: {result_amount}')
