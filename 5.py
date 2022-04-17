# Дано число. Проверить кратно ли оно 5 и 10 или 15 но не 30

def compare(x):
    if (((x % 5 == 0) and (x % 10 == 0)) or ((x % 15 == 0) and (x % 30 != 0))):
        print (x % 5, x % 10, x % 15, x % 30)
        print('Условия соблюдаются')
    else:
        print (x % 5, x % 10, x % 15, x % 30)
        print('Условия не соблюдаются')


number = int(input('Введите число '))
compare(number)
