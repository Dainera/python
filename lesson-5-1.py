# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

def write_file(f, text=None):
    if text:
        f.write(f'{text}\n')


file = open('test_file.txt', 'w', encoding='utf-8')

while True:
    text_line = input('Enter new line: ')
    if text_line == '' or text_line == ' ':
        break
    write_file(file, text_line)

file.close()
