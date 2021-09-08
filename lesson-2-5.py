# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

rating_list = [7, 5, 3, 3, 2]

new_rating = None

while new_rating != -1:
    print(f"Rating: {rating_list} len: {len(rating_list)} min: {min(rating_list)} max: {max(rating_list)}")
    new_rating = int(input("Enter rating number (-1 to exit): "))

    if new_rating <= 0 and new_rating != -1:
        print('Must be natural number')
        continue

    if new_rating > max(rating_list):
        rating_list.insert(0, new_rating)
    elif new_rating < min(rating_list) or new_rating == min(rating_list):
        rating_list.append(new_rating)
    else:
        for i in range(len(rating_list)):
            if rating_list[i + 1] < new_rating < rating_list[i]:
                rating_list.insert(i + 1, new_rating)
                break
            elif rating_list[i] == new_rating:
                rating_list.insert(i + 1, new_rating)
                break
