# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

file = open('lesson-5-2-data.txt', 'r', encoding='utf-8')

line_count = 0
words_in_lines = {}

for i, line in enumerate(file.readlines()):
    words_in_lines[i] = f'{len(line.split())} words: {line}'
    line_count += 1

file.close()

print(f'Line count: {line_count}')

for key, value in words_in_lines.items():
    print(f'In {key} line {value}')
