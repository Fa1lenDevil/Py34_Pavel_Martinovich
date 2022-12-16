"""создать 2 класса truck, car, которые являются наследниками класса ауто. Класс трак имеет дополнительный обязательный атрибут
max_load. Переопределенный метод move, перед появлением надписи move выводит надпись attention. Также доп метод лоад.
При его вызове происходит пауза 1 сек, затем выдается сообщение лоад и снова пауза на 1 сек. Класс кар имеет доп обязательный
атрибут макс_спид, и при вызове метода мув, после появления надписи мув должна появиться надпись макс_спид. Создать по 2 объекта
каждого из классов трак и кар, проверить все методы и атрибуты."""
import time


class Auto:


    def __init__(self, brand, mark, age, color, weight):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        self.age += 1
        print(self.age)


class Truck(Auto):
    max_load = 2500

    def __init__(self, brand, mark, age, color, weight):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print('attention')
        time.sleep(1)
        print(self.brand, self.mark, 'is moving')

    def load(self):
        time.sleep(1)
        print(self.brand, self.mark, 'is loading')
        time.sleep(1)

class Car(Auto):

    def __init__(self, brand, mark, age, color, weight, max_speed):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight
        self.max_speed = max_speed

    def move(self):
        print(self.brand, self.mark, 'is moving')
        print('max speed is', self.max_speed)


man = Truck('Man','b350', 2, 'red', 4500)
volvo = Truck('Volvo','FH16', 1, 'white', 3200)
bmw = Car('BMW','520d', 3, 'black', 1800, 250)
alfa = Car('Alfa-romeo','Guilia', 2, 'yellow', 1700, 270)

man.load()
man.move()
volvo.load()
volvo.move()
bmw.move()
alfa.move()
alfa.stop()