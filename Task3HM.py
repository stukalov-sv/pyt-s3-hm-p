# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def random_float_fill_list(size: int) -> list:
    result_list = []
    for i in range(size):
        result_list.append(round(random.uniform(0, 11), 3))
    return result_list

def fractional_parts_subtract(user_list: list) -> float:
    max_fract_part = float(user_list[0] - int(user_list[0]))
    min_fract_part = float(user_list[0] - int(user_list[0]))

    for i in range(len(user_list)):
        if (type(user_list[i]) == float): # для исключения int
            if (user_list[i] - int(user_list[i]) > max_fract_part):
                max_fract_part = round(user_list[i] - int(user_list[i]), 3)
            elif (user_list[i] - int(user_list[i]) < min_fract_part):
                min_fract_part = round(user_list[i] - int(user_list[i]), 3)
        else:
            i += 1
    print(max_fract_part, min_fract_part)
    result_subtract = round(max_fract_part - min_fract_part, 3)
    return result_subtract

random_list = random_float_fill_list(int(input('Enter list length: ')))
# random_list = [1.1, 1.2, 3.1, 5, 10.01] # для проверки примера
print(f'Random list:\n{random_list}')

print('Max and min fractional parts of elements in list:')
result_subtract = fractional_parts_subtract(random_list)

print(f'Max and min fractional parts subtract of elements in list:\n{result_subtract}')
