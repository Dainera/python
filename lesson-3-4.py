# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами. Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.


def my_func(x, y):
    return 1 / x ** abs(y)


def my_func_cycle(x, y):
    num = 1

    for i in range(abs(y)):
        num *= x

    return 1 / num


first_arg = int(input('Enter first argument: '))
second_arg = int(input('Enter second argument: '))

print(f'Result: {my_func(first_arg, second_arg)}')
print(f'Result with cycle: {my_func_cycle(first_arg, second_arg)}')

