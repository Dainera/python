# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать
# число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    data_string = None
    date_parts = None

    def __init__(self, data_string):
        Date.data_string = data_string

    @classmethod
    def get_data_as_num(cls):
        try:
            Date.date_parts = list(map(int, Date.data_string.split('-')))
            return Date.date_parts
        except ValueError:
            return 'Invalid date'
        except AttributeError:
            return 'Date not set'

    @staticmethod
    def validate_date():
        try:
            if 1 <= Date.date_parts[0] <= 31 and 1 <= Date.date_parts[1] <= 12 and 1901 <= Date.date_parts[2]:
                return True
            else:
                return False
        except TypeError:
            return 'Date not set or is invalid'
        except IndexError:
            return 'Date not set or is invalid'


date = Date('01-01-2021')
print(Date.get_data_as_num())
print(Date.validate_date())

