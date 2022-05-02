# Написать программу преобразования десятичного числа в двоичное

n = int(input('Введите десятичное число '))
list = []
while n > 0:
    list.append(n % 2)
    n = n//2

list1 = list[::-1]

s = "".join(map(str, list1))
print('Двоичное число', s)
