# Найти максимальное из пяти чисел

def Maximum(a, b, c, d, e):
    max = a
    if (b > max):
        max = b
    if (c > max):
        max = c
    if (d > max):
        max = d
    if (e > max):
        max = e
    print('Максимальное число ', max)


number1 = float(input('Введите первое число '))
number2 = float(input('Введите второе число '))
number3 = float(input('Введите третье число '))
number4 = float(input('Введите четвертое число '))
number5 = float(input('Введите пятое число '))

Maximum(number1, number2, number3, number4, number5)
