# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.


month_num = int(input("Enter month number (1 to 12): "))

seasons_dict = {'Winter': (1, 2, 12),
                'Spring': (3, 4, 5),
                'Summer': (6, 7, 8),
                'Autumn': (9, 10, 11)
                }

for s_key in seasons_dict.keys():
    if month_num in seasons_dict[s_key]:
        print(f'Dictionary says that your season is: {s_key}')

seasons_list = ['Winter', 'Spring', 'Summer', 'Autumn']

if month_num in range(1, 3) or month_num == 12:
    print(f'List says that your season is: {seasons_list[0]}')
elif month_num in range(3, 6):
    print(f'List says that your season is: {seasons_list[1]}')
elif month_num in range(6, 9):
    print(f'List says that your season is: {seasons_list[2]}')
elif month_num in range(9, 12):
    print(f'List says that your season is: {seasons_list[3]}')