"""Создать класс Прямоугольник, который имеет свойства Ширина и Высота.
Также добавить свойство для нахождения площади. Свойства реализовать через property."""

class Rectangle:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @a.setter
    def a(self, value):
        self._a = value

    @b.setter
    def b(self, value):
        self._b = value

    @property
    def S(self):
        return rect.a*rect.b

rect = Rectangle(4, 5)
print(rect.S)







