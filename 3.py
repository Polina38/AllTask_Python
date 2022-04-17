# Вывести на экран числа от -N до N

number = int(input('Введите число '))

r = range(-number, number, 1)
for i in r:
    print(i)
