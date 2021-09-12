# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(first, second, third):
    args_range = [first, second, third]
    args_range.remove(min(args_range))
    return sum(args_range)


first_arg = int(input('Enter first argument: '))
second_arg = int(input('Enter second argument: '))
third_arg = int(input('Enter third argument: '))

print(f'Result {my_func(first_arg, second_arg, third_arg)}')
