# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание,
# что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle

start_num = int(input('Enter some start number: '))

last_iteration = start_num + 10

for i in count(start_num):
    print(i)
    if i > last_iteration:
        break


elements = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
last_iteration = len(elements) * 3
i = 0

print('\nPredefined elements with cycle: ')

for el in cycle(elements):
    print(el)
    i += 1
    if i >= last_iteration:
        break
    if i % len(elements) == 0:
        print("\n")
