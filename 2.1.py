# Пользователь вводит время в секундах. Переведите время в часы, минуты,
# секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

def Time(x):
    if (x < 60):
        print(f'00:00:{x}')
    elif (x > 60 and x < 360):
        y = x//60
        x = x-y*60
        print(f'00:{y}:{x}')
    else:
        z = x//3600
        y = (x-z*3600)//60
        x = x-z*3600-y*60
        print(f'{z}:{y}:{x}')


n1 = int(input('Введите время в секундах  '))
Time(n1)