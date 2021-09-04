# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
#    Используйте форматирование строк.


seconds = int(input('Enter time in seconds: '))

hours = seconds // 3600
seconds_rem = int(seconds % 60)
minutes = seconds // 60
minutes_rem = int(minutes % 60)

print(f'Entered time {hours:02d}:{minutes_rem:02d}:{seconds_rem:02d}')
