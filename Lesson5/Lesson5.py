#Создать функцию для генерации списков.
#Функция должна возвращать сгенерированный список чисел
#Пример использования функции:
#A = Generator(start = 10, stop = 20, step = 2) #### A[10,12,14,16,18]
#A = Generator(start = 5, stop = 10) #### A[5,6,7,8,9]

def generator(start: int, stop: int, step: int) -> list:
    start = int(input('С какого числа? '))
    stop = int(input('По какое число? '))
    step = int(input('Какой шаг генерации? '))
    if step > 0:
        list1 = [i for i in range(start, stop, step)]
        print(list1)
    else:
        list1 = [i for i in range(start, stop)]
        print(list1)
generator(1,1,1)

import time

"""Сделать функцию которая будет вызываться из генератора списка и по запросу к ней
отдавать текущее время с задержкой в 1 сек. Кол-во элементов нового списка n запрашивать у пользователя."""
import datetime


def TimeData():
    list1 = []
    n = int(input('Введите количество элементов: '))
    for i in range(1, n+1):
        time.sleep(1)
        DateNow = datetime.datetime.now()
        DateNowStr = DateNow.strftime('%Y/%m/%d %H:%M:%S')
        list1.append(DateNowStr)
        print(list1)
TimeData()