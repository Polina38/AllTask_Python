#По двум заданным числам проверить является ли одно квадратом второго


def compare (x,y):
    if (x==y**2 or y==x**2):
        print ('Одно число яляется квадратом другого')
    else: print ('Ни одно число не является квадратом другого')


number1= int(input('Введите первое число  '))
number2= int(input ('Введите второе число  '))

compare (number1,number2) 
