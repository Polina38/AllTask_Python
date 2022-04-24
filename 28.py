# Найти корни квадратного уравнения Ax² + Bx + C = 0
# Математикой
# Используя дополнительные библиотеки*

# def Quadratic(x, y, z):
#     Discrim = y*y-4*x*z
#     if (Discrim < 0):
#         print('Корней нет')
#     elif (Discrim == 0):
#         itog1 = (-y/(2*x))
#         print('Один корень и он равен ', itog1)
#     else:
#         itog1 = round(((-y - Discrim**0.5)/(2*x)), 2)
#         itog2 = round(((-y + Discrim**0.5)/(2*x)), 2)
#         print(f'Первый корень равен ', itog1, 'Второй корень равен ', itog2)


# a = int(input('Введите значение А в Ax² '))
# b = int(input('Введите значение B в Bx '))
# c = int(input('Введите значение C '))
# Quadratic(a, b, c)


# Второй вариант сиспользование библиотек:

from cmath import sqrt
import math

def Quadratic(x, y, z):
    Discrim = math.pow(y,2)-4*x*z
    if (Discrim < 0):
        print('Корней нет')
    elif (Discrim == 0):
        itog1 = (-y/(2*x))
        print('Один корень и он равен ', itog1)
    else:
        itog1 = round(((-y - math.sqrt(Discrim))/(2*x)), 2)
        itog2 = round(((-y + math.sqrt(Discrim))/(2*x)), 2)
        print(f'Первый корень равен ', itog1, 'Второй корень равен ', itog2)


a = int(input('Введите значение А в Ax² '))
b = int(input('Введите значение B в Bx '))
c = int(input('Введите значение C '))
Quadratic(a, b, c)

