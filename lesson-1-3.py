# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
#    Считаем 3 + 33 + 333 = 369.


number = int(input('Enter some number: '))

number_twice = int(f'{number}{number}')
number_thrice = int(f'{number}{number}{number}')

print(f'Result number {number + number_twice + number_thrice}')
