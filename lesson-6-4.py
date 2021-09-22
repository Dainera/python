# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} start moving')

    def stop(self):
        print(f'{self.name} stop moving')

    def turn(self, direction):
        print(f'{self.name} turned to the {direction}')

    def show_speed(self):
        print(f'{self.name} speed: {self.speed}')


class TownCar(Car):

    def show_speed(self):
        print(f'{self.name} speed: {self.speed}')
        if self.speed > 60:
            print(f'You are going too fast!')


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        print(f'{self.name} speed: {self.speed}')
        if self.speed > 40:
            print(f'You are going too fast!')


class PoliceCar(Car):
    pass


town_car = TownCar(80, 'red', 'Town Car', False)
work_car = WorkCar(60, 'yellow', 'Work Car', False)
sport_car = SportCar(280, 'white', 'Sport Car', False)
police_car = PoliceCar(100, 'blue', 'Police Car', True)

town_car.go()
town_car.turn('left')
town_car.turn('right')
town_car.show_speed()
town_car.stop()
print('\n')
work_car.go()
work_car.turn('left')
work_car.turn('right')
work_car.show_speed()
work_car.stop()
print('\n')
sport_car.go()
sport_car.turn('left')
sport_car.turn('right')
sport_car.show_speed()
sport_car.stop()
print('\n')
police_car.go()
police_car.turn('left')
police_car.turn('right')
police_car.show_speed()
police_car.stop()