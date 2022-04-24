# Строка содержит набор чисел. Показать большее и меньшее число
# Символ-разделитель - пробел

def Min_Max_spisok(str):
    new_str = str.split(' ')
    min = int(new_str[0])
    max = int(new_str[0])

    for i in range(len(new_str)):
        new_str[i] = int(new_str[i])
        if (new_str[i] < min):
            min = new_str[i]
        if (new_str[i] > max):
            max = new_str[i]

    print(f'Наименьшее число в списке ', min,
          'Наибольшее число в списке ', max)


my_str = input('Введите несколько цифр, используя пробел для их разделения ')
Min_Max_spisok(my_str)
