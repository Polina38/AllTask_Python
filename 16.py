# Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму


n = int(input('Введите n '))

list = [pow((1+1/i), i) for i in range(1, n+1)]

print(list)

print('Сумма чисел последовательности ', sum(list))
