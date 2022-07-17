# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
#
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def positive_fibonacci(user_number: int) -> list:
    fib_list = [0, 1]

    for i in range(2, user_number + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])

    return fib_list

def negative_fibonacci(user_number: int) -> list:
    fib_list = [0, 1]

    for i in range(2, user_number + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])

    for i in range(2, user_number + 1):
        if (i % 2 == 0):
            fib_list[i] = -fib_list[i]

    return fib_list

user_number = int(input('Enter decimal number to convert: '))
fib_positive = positive_fibonacci(user_number)
del fib_positive[0]
fib_negative = negative_fibonacci(user_number)
fib_negative.reverse()

result_fibonacci = fib_negative + fib_positive
print(f'Fibbonacci series for positive and negative values:\n{result_fibonacci}')
