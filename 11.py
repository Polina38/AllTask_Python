# Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.


n1 = int(input('Введите число N  '))

numbers = list(range(n1))
numbers[0] = 1
for i in range(1, n1):
    numbers[i] = -3*numbers[i-1]
    print(numbers)
