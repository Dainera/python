# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}


def find_lesson_hours(hours_data):
    hours = 0
    for el in hours_data.split():
        try:
            idx = el.index('(')
            hours += int(el[:idx])
        except ValueError:
            continue
    return hours


file = open('lesson-5-6-data.txt', 'r', encoding='utf-8')

dict_lessons = {}

for line in file.readlines():
    key = line.split(':')
    dict_lessons[key[0]] = find_lesson_hours(key[1])

file.close()

print(dict_lessons)

