# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.

from time import sleep


class TrafficLight:
    __color = None
    __colors_dict = {'red': 7, 'yellow': 2, 'green': 4}

    def __init__(self):
        self.TrafficLight = None

    def running(self, cycles):
        i = 0
        while True:
            for key, value in TrafficLight.__colors_dict.items():
                self.__color = key
                print(self.__color)
                sleep(value)
            i += 1
            if i > cycles:
                print('Enough..')
                break


light = TrafficLight()

light.running(3)
