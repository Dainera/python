# 5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
# передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц
# оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

class Storage:

    def __init__(self):
        self.__storage_dict = {}

    @property
    def storage_dict(self):
        return self.__storage_dict.copy()

    def move_to_department(self, equipment, count):
        identity = equipment.get_identity()
        if identity in self.__storage_dict:
            if self.__storage_dict[identity] > count:
                self.__storage_dict[identity] -= count
            else:
                print('There are not enough equipments in the storage')
        else:
            print('There is no equipment of this type and model in the storage')

    def receive_equipment(self, equipment, count):
        identity = equipment.get_identity()
        if identity in self.__storage_dict:
            self.__storage_dict[identity] += count
        else:
            self.__storage_dict[identity] = count

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


storage = Storage()

storage.receive_equipment(Printer('A51', 'Zerox', 50), 3)
storage.receive_equipment(Printer('A51A', 'Zerox', 50), 1)
storage.receive_equipment(Scanner('A51A', 'Alfo4', 50), 2)

copier = Copier('A51A', '36', 50)

storage.receive_equipment(copier, 45)

print(storage.get_storage_equipments())

storage.move_to_department(copier, 5)

print(storage.get_storage_equipments())

storage.move_to_department(Copier('R51A', '36', 50), 10)
storage.move_to_department(copier, 500)

