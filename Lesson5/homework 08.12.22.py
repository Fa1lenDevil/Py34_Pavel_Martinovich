# Дан список чисел. Вернуть список, где при помощи функции map()
# каждое число переведено в строку. В качестве функции в map() использовать lambda
import time

Numbers = [1, 2, 4, 63, 12, 31, 63, 645, 84, 55, 43, 9, 90, 6]
strlist = map(lambda x: str(x), Numbers)
print(list(strlist))

# Написать декоратор к 2-м любым функциям, который бы считал и выводил время их выполнения.


def my_decorator(func_to_decorate):
    def wrapper():
        from datetime import datetime
        time1 = datetime.now()
        func_to_decorate()
        time2 = datetime.now()
        worktime = (time2 - time1)
        print(worktime)
    return wrapper()


@my_decorator
def TimeData():
    import datetime
    list1 = []
    n = int(input('Введите количество элементов: '))
    for i in range(1, n+1):
        time.sleep(1)
        DateNow = datetime.datetime.now()
        DateNowStr = DateNow.strftime('%Y/%m/%d %H:%M:%S')
        list1.append(DateNowStr)
    print(list1)


TimeData()


@my_decorator
def Main_Triangle():
    import turtle
    import colorsys
    t = turtle.Turtle()
    t.screen.bgcolor('black')
    t.penup()
    t.goto(-200, -100)
    t.pendown()
    t.speed(10)
    a = 400
    h = 0
    n = 100

    def triangle():
        nonlocal a, n, h
        for i in range(40):
            c = colorsys.hsv_to_rgb(h, 1, 0.6)
            h = h + (1/n)
            t.color(c)
            t.forward(a)
            t.left(120)
            a = a - 10
    triangle()
    triangle()
    t.hideturtle()
Main_Triangle()
