# Сообщить в какой четверти координатной плоскости
# или на какой оси находится точка с координатами Х и У

def seach_point(x, y):
    if (x > 0 and y > 0):
        print('Точка в I четверти координатной плоскости')
    elif(x < 0 and y > 0):
        print('Точка в II четверти координатной плоскости')
    elif(x < 0 and y < 0):
        print('Точка в III четверти координатной плоскости')
    elif(x > 0 and y < 0):
        print('Точка в IV четверти координатной плоскости')
    elif(x == 0):
        print('Точка лежит на оси Y')
    else:
        print('Точка лежит на оси X')


number1 = int(input('Введите значение Х  '))
number2 = int(input('Введите значение Y  '))
seach_point(number1, number2)
