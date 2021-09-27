# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа:
# V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма
# (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def calculate_fabric_expense(self):
        pass


class Coat(Clothes):

    def __init__(self, s):
        self.size = s

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, s):
        if s < 0:
            self.__size = 0
        else:
            self.__size = s

    def calculate_fabric_expense(self):
        return round(self.__size / 6.5 + 0.5, 2)


class Suit(Clothes):

    def __init__(self, h):
        self.height = h

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        if h < 0:
            self.__height = 0
        else:
            self.__height = h

    def calculate_fabric_expense(self):
        return round(2 * self.height + 0.3, 2)


coat = Coat(40)
print(f'Coat expense: {coat.calculate_fabric_expense()}')

suit = Suit(165)
print(f'Suit expense: {suit.calculate_fabric_expense()}')

