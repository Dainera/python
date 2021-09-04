# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
#    Для решения используйте цикл while и арифметические операции.

positive_number = int(input('Enter some positive number: '))

max_number = -1

while positive_number > 0:
    current_number = int(positive_number % 10)
    if max_number < current_number:
        max_number = current_number
    positive_number /= 10

print(f'Max number is: {max_number}')