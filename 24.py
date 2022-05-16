# В заданном списке вещественных чисел найдите разницу между максимальным
# и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19


my_spisok = [1.19, 0.87, 0.9, 0.53, 0.21, 4.05, 0.62, 3]


def NumberTail(list):
    list1 = []
    for item in range(len(list)):
        elem = str(list[item])
        elem = elem.split('.')
        if len(elem) < 2:
            element1 = 0
        else:
            element1 = int(elem[1])
        list1.append(element1)
    max = list1[0]
    min = list1[0]
   
    for item in range(len(list1)):
        if (list1[item] > max):
            max = list1[item]

        if (list1[item] < min and list1[item] != 0):
            min = list1[item]
    result1 = '0.'
    result1 = result1+str(max-min)
    return print('Разница между максимальным и минимальным значением дробной части элементов ', result1)


NumberTail(my_spisok)
