# Определить, присутствует ли в заданном списке строк, некоторое число

def Identification(spisok, element):
    flag = False
    for item in spisok:
        if (item == element):
            flag = True
            break

    if flag:
        print('Заданное число присутствует ')
    else:
        print('Заданного числа в списке нет ')


my_spisok = [134, 34, 786, 567, 406, 89, 901]
a = 406


Identification(my_spisok, a)
