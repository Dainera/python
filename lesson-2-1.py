# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

some_list = ['Hello', 1, 1.1, float(9), bytes([2, 3, 4]), bytearray(6), frozenset('python'), None,
             complex(2, 5), (1, 2), True, {3, 4, 'World'}, {'name': 'London1'}]

for el in some_list:
    type_el = type(el)
    print(f'{el}: {type_el}')

    if type_el == str:
        print(f'String! Cool!')
        print(f'isdigit: {el.isdigit()}')
        print(f'isnumeric: {el.isnumeric()}')
        print(f'isdecimal: {el.isdecimal()}')
        print(f'isascii: {el.isascii()}')
        print(f'isalnum: {el.isalnum()}')
        print(f'isalpha: {el.isalpha()}\n')
    elif type_el == float:
        print(f'is_integer: {el.is_integer()}\n')
    elif type_el == int:
        print('Is integer - cool!\n')
    elif type_el == bytes:
        print('Bytes!\n')
    elif type_el == bytearray:
        print('Bytearray, nice!\n')
    elif type_el == frozenset:
        print('Frozenset.. \n')
    elif type_el == complex:
        print('Complex \n')
    elif type_el == bool:
        print('Boolean \n')
    elif type_el == type(None):
        print(f'None type\n')
    elif type_el == tuple:
        print(f'Tuple\n')
    elif type_el == set:
        print(f'Set of elements\n')
    elif type_el == dict:
        print(f'Dictionary, that is all?\n')
    else:
        print('\n')
