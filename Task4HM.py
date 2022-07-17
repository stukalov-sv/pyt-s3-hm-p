# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def decimal_to_binary(user_number: int) -> str:
    result_binary_list = []

    while (user_number >= 1):
        remainder = user_number % 2
        result_binary_list.append(remainder)
        user_number = user_number // 2

    temp_binary_str = ''.join(map(str, result_binary_list))
    result_binary_str = temp_binary_str[::-1]
    return result_binary_str

user_number = int(input('Enter decimal number to convert: '))
binary_number = decimal_to_binary(user_number)

print(f'Binary value: {binary_number}')
