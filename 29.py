# Считайте два числа из файла (одно число в одной строке). Напишите программу, которая найдёт НОК
# (наименьшее общее кратное) этих двух чисел.
import math


my_spisok = []
path = 'support.txt'
data = open(path, 'r')
for line in data:
    my_spisok.append(line)
data.close()
for i in range(len(my_spisok)):
    my_spisok[i] = int(my_spisok[i])

    
print(my_spisok)

a = math.lcm(my_spisok[0], my_spisok[1])
print('Наименьшее общее кратное равно ', a)

# itog1 = my_spisok[0]*my_spisok[1]
# count = 2
# delitel = 1
# while count < 10:
#     if (my_spisok[0] % count == 0 and my_spisok[1] % count == 0):
#         delitel = count
#         break
#     else:
#         count += 1

# print('Наименьшее общее кратное равно ', itog1/delitel)
