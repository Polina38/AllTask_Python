# В заданном списке вещественных чисел найдите разницу между максимальным
# и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19


my_spisok = [1.19, 0.87, 0.9, 0.53, 0.21, 4.05, 0.62, 3]
max = my_spisok[0]
min = my_spisok[0]
for item in range(len(my_spisok)):
    if (my_spisok[item] > max):
        max = my_spisok[item]
    if (my_spisok[item] < min):
        min = my_spisok[item]

print(max-min)
