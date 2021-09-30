# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте
# перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры
# класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

from lesson_8_3 import NotANumberError


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        try:
            ComplexNumber.validate_input(value)
            self.__a = value
        except NotANumberError as e:
            print(e)
            self.__a = 0

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        try:
            ComplexNumber.validate_input(value)
            self.__b = value
        except NotANumberError as e:
            print(e)
            self.__b = 0

    @staticmethod
    def validate_input(value):
        if (not isinstance(value, int)) and (not isinstance(value, float)):
            raise NotANumberError('Value must be an integer or float')

    def __add__(self, other):
        return ComplexNumber(self.a + other.b, self.b + other.b)

    def __mul__(self, other):
        return ComplexNumber((self.a * other.a - self.b * other.b), (self.b * other.a + self.a * other.b))

    def __str__(self):
        return f'{self.a} + {self.b}j'


first_complex = ComplexNumber(5, 1)
second_complex = ComplexNumber(2, 3)

print(first_complex + second_complex)
print(first_complex * second_complex)

first_complex = ComplexNumber(5.3, 1.5)
second_complex = ComplexNumber(1.2, 7.2)

print(first_complex + second_complex)
print(first_complex * second_complex)