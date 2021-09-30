# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

from lesson_8_3 import NotANumberError


class NotAnEquipment(Exception):

    def __init__(self, msg):
        self.msg = msg


class Storage:

    def __init__(self):
        self.__storage_dict = {}

    @property
    def storage_dict(self):
        return self.__storage_dict.copy()

    @staticmethod
    def validate_input(equipment, count):
        if not isinstance(count, int):
            raise NotANumberError('Count must be integer')
        if not issubclass(equipment.__class__, OfficeEquipment):
            raise NotAnEquipment('Storage can manage only Office Equipments')

    def move_to_department(self, equipment, count):
        try:
            Storage.validate_input(equipment, count)
            identity = equipment.get_identity()
            if identity in self.__storage_dict:
                if self.__storage_dict[identity] > count:
                    self.__storage_dict[identity] -= count
                else:
                    print('There are not enough equipments in the storage')
            else:
                print('There is no equipment of this type and model in the storage')
        except NotAnEquipment as e:
            print(e)
        except NotANumberError as e:
            print(e)

    def receive_equipment(self, equipment, count):
        try:
            Storage.validate_input(equipment, count)
            identity = equipment.get_identity()
            if identity in self.__storage_dict:
                self.__storage_dict[identity] += count
            else:
                self.__storage_dict[identity] = count
        except NotANumberError as e:
            print(e)
        except NotAnEquipment as e:
            print(e)

    def get_storage_equipments(self):
        return self.__storage_dict


class OfficeEquipment:

    def __init__(self, model, manufacturer):
        self.model = model
        self.manufacturer = manufacturer

    def get_identity(self):
        return f'{self.get_name()} {self.manufacturer} {self.model}'

    @classmethod
    def get_name(cls):
        return cls.__name__


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


def check_stop(val):
    if val.lower() == 'stop':
        print(storage.get_storage_equipments())
        exit(1)


def get_count():
    while True:
        val = input('Enter equipment count: ')
        check_stop(val)
        try:
            if not val.isnumeric():
                raise NotANumberError('Not A Number')
        except NotANumberError as e:
            print(e)
            continue
        return int(val)


def create_copier():
    return Copier(input('Enter COPIER Model: '), input('Enter COPIER Manufacturer: '),
                  input('Enter COPIER copy speed: '))


def create_printer():
    return Printer(input('Enter PRINTER Model: '), input('Enter PRINTER Manufacturer: '),
                   input('Enter PRINTER max paper: '))


def create_scanner():
    return Printer(input('Enter SCANNER Model: '), input('Enter SCANNER Manufacturer: '),
                   input('Enter SCANNER color depth: '))


def add_equipment():
    while True:
        val = input('Enter equipment type number (PRINTER: type 1, SCANNER: type 2, COPIER: type 3, return 4): ')
        check_stop(val)
        if val == '1':
            count = get_count()
            storage.receive_equipment(create_printer(), count)
        elif val == '2':
            count = get_count()
            storage.receive_equipment(create_scanner(), count)
        elif val == '3':
            count = get_count()
            storage.receive_equipment(create_copier(), count)
        elif val == '4':
            break


def move_equipment():
    while True:
        val = input('Enter equipment type number (PRINTER: type 1, SCANNER: type 2, COPIER: type 3, return 4): ')
        check_stop(val)
        if val == '1':
            count = get_count()
            storage.move_to_department(create_printer(), count)
        elif val == '2':
            count = get_count()
            storage.move_to_department(create_scanner(), count)
        elif val == '3':
            count = get_count()
            storage.move_to_department(create_copier(), count)
        elif val == '4':
            break


if __name__ == "__main__":

    storage = Storage()

    while True:
        print(f'Equipnents in storage: {storage.get_storage_equipments()}', end='\n')
        value = input('Type ADD to add equipment, MOVE to move equipment and STOP to exit: ')
        check_stop(value)

        if value.lower() == 'add':
            add_equipment()

        elif value.lower() == 'move':
            move_equipment()
