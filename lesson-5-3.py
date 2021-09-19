# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


file = open('lesson-5-3-data.txt', 'r', encoding='utf-8')

average_salary = 0
employees = {}

for line in file.readlines():
    data = line.split()
    employees[data[0]] = int(data[1])
    average_salary += employees[data[0]]

file.close()

average_salary = average_salary / len(employees.items())

print(f'Average salary: {average_salary} thous.')

for key, value in employees.items():
    if value < 20:
        print(f'{key} with salary {value} thous.')
