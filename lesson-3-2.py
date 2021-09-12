# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.


def show_user_info(f_name, l_name, dob_year, city, email, phone):
        print(f_name, l_name, dob_year, city, email, phone, sep=", ")


first_name = input('Enter First Name: ')
last_name = input('Enter Last Name: ')
year = int(input('Enter Date of Birth year: '))
living_city = input('Enter City: ')
user_email = input('Enter Email: ')
user_phone = input('Enter Phone: ')

show_user_info(f_name=first_name, l_name=last_name, dob_year=year, city=living_city, email=user_email, phone=user_phone)