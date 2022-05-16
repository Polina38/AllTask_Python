# Даны два файла, в каждом из которых находится запись квадратного многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


from encodings import utf_8

path = 'support34.1.txt'
data = open(path, 'r')
data1 = data.read()
data.close()

path = 'support34.2.txt'
data = open(path, 'r')
data2 = data.read()
data.close()


def FindCoef(filenew):
    list = filenew.split('x')
    Coef1 = list[0]
    number = '1234567890'
    Coef2 = ''
    for ch in list[-2]:
        if ch == "-" or ch == "+" or ch in number:
            Coef2 = Coef2+ch
    Coef3 = list[-1]
    spisok = []
    spisok.append(int(Coef1))
    spisok.append(int(Coef2))
    spisok.append(int(Coef3))
    print(spisok)
    return (spisok)


mylist = list(map(sum, zip(FindCoef(data1), FindCoef(data2))))

print(mylist)
on1 = ''
if mylist[1] > 0:
    on1 = on1+"+"
on2 = ''
if mylist[2] > 0:
    on2 = on2+"+"

itog = f'{mylist[0]}x²{on1}{mylist[1]}x{on2}{mylist[2]}'
print(itog)

with open('support34.sum.txt', 'w',encoding='utf_8') as data:
    data.write(itog)
