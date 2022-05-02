# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]


n = int(input('Введите число N '))


def recurs(x):

    if x <= 1:
        return 1
    else:
        return x*recurs(x-1)


my_list = [recurs(i) for i in range(1, n+1)]
print(my_list)
