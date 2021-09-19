# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
from json import dump

dict_profit = {}
average_profit = 0
firms_count = 0

with open('lesson-5-7-data.txt', 'r', encoding='utf-8') as file:
    for line in file.readlines():
        try:
            firm_data = line.split()
            name = firm_data[0]
            if name != '':
                firms_count += 1
                earnings = int(firm_data[2])
                costs = int(firm_data[3])
                profit = earnings - costs
                dict_profit[name] = profit
                if profit > 0:
                    average_profit += profit
        except ValueError:
            continue

average_profit = round(average_profit / firms_count, 2)
firms_list = [dict_profit, {'average_profit': average_profit}]

print(firms_list)

with open('lesson-5-7-data.json', 'w', encoding='utf-8') as new_file:
    dump(firms_list, new_file)