# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и
# премия, например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом
# премии (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).

class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


barber = Position('Ivan', 'Ivanov', 'barber', 10000, 250)
manager = Position('Hans', 'Andersen', 'manager', 50000, 3000)
developer = Position('Jhon', 'Doe', 'developer', 100000, 0)

print(f'{barber.get_full_name()} has income: {barber.get_total_income()}')
print(f'{manager.get_full_name()} has income: {manager.get_total_income()}')
print(f'{developer.get_full_name()} has income: {developer.get_total_income()}')