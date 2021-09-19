# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from random import randint


def write_file(f, text=None):
    if text:
        f.write(f'{text}\n')


file = open('lesson-5-5-data.txt', 'w+', encoding='utf-8')

for i in range(0, 10):
    if i > 0:
        file.write(f' ')
    file.write(str(randint(0, 100)))

file.flush()
file.seek(0)

numbers_str = file.read()

print(f'Numbers: {numbers_str}')

numbers = numbers_str.split()

file.close()

numbers_sum = 0

for num in numbers:
    if num.isdigit():
        numbers_sum += int(num)

print(f'Numbers sum: {numbers_sum}')
