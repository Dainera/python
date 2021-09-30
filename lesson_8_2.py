# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

def divide_by_zero_check(dividend, divisor):
    try:
        if divisor == 0:
            raise DivideByZeroError('Division by zero')
        return dividend / divisor
    except DivideByZeroError as e:
        print(e)


class DivideByZeroError(Exception):

    def __init__(self, msg):
        self.msg = msg


num = int(input('Enter number: '))
num_divisor = int(input('Enter divisor: '))

print(divide_by_zero_check(num, num_divisor))