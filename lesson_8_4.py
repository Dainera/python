# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

class Storage:
    pass


class OfficeEquipment:

    def __init__(self, model, manufacturer):
        self.model = model
        self.manufacturer = manufacturer


class Printer(OfficeEquipment):

    def __init__(self, model, manufacturer, max_paper):
        self.max_paper = max_paper
        super().__init__(model, manufacturer)


class Scanner(OfficeEquipment):

    def __init__(self, model, manufacturer, color_depth):
        self.color_depth = color_depth
        super().__init__(model, manufacturer)


class Copier(OfficeEquipment):
    def __init__(self, model, manufacturer, copy_speed):
        self.copy_speed = copy_speed
        super().__init__(model, manufacturer)
