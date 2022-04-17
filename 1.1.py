# Посчитать факториал числа n

def Factarial(x):
    if (x <= 0):
        a = 1
    else:
        a = x
    while x > 1:
        a = a*(x-1)
        x = x-1
    print(a)


n1 = int(input('Введите число N  '))
Factarial(n1)
