# Найти расстояние между двумя точками пространства

import math


def find_distance(x1, y1, x2, y2):
    a = math.sqrt((y2-y1)**2+(x2-x1)**2)
    print('Расстояние между точками ', round(a, 2))


number1 = int(input('Введите коррдинату первой точки X1  '))
number2 = int(input('Введите коррдинату первой точки Y1  '))
number3 = int(input('Введите коррдинату второй точки X2  '))
number4 = int(input('Введите коррдинату второй точки Y2  '))

find_distance(number1, number2, number3, number4)
