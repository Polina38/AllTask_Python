# Показать первую цифру дробной части числа

def first_number(x):
    x = x*10
    x = x % 10
    print(round(x//1))


number = float(input('Введите дробное число '))
first_number(number)
