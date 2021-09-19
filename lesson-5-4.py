# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


file = open('lesson-5-4-data.txt', 'r', encoding='utf-8')
new_file = open('lesson-5-4-data-new.txt', 'w+', encoding='utf-8')

words = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

for line in file.readlines():
    for key in words:
        if key in line:
            new_line = line.replace(key, words[key])
            new_file.write(new_line)

file.close()
new_file.flush()
new_file.seek(0)

print(new_file.read())

new_file.close()