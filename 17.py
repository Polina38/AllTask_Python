# Задать список из N элементов, заполненных числами из [-N, N].
# Найти произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число

n = int(input('Введите значение N '))

list = [i for i in range(-n, n+1)]

print(list)

file = open('file.txt', 'w')
for i in range(len(list)):
    file.write(str(i)+'\n')
file.close

list1 = [i*list[i] for i in range(len(list))]
print(list1)
