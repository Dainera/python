# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def divide(dividend, divider):
    try:
        return dividend / divider
    except ZeroDivisionError:
        return "Division by 0"


first = int(input('Enter first number: '))
second = int(input('Enter second number: '))

print(f"Division result: {divide(first, second)}")