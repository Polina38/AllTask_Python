# Дано число. Составить список чисел Фибоначчи, в том числе для отрицательных индексов.
#  Т е для k = 8, список будет выглядеть так: [-21 ,13, -8, 5, −3,  2, −1,  1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Негафибоначчи


n = int(input('Введите число N '))


def recurs(x):
    if x == 0:
        return 0
    elif x == 1 or x == -1:
        return 1
    elif x > 0:
        return recurs(x-1)+recurs(x-2)
    else:
        return recurs(x+2)-recurs(x+1)


list = [recurs(i) for i in range(-n, n+1)]
print(list)
