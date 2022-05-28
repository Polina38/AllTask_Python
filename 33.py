# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# а0хn + а1хn-1 + а2хn-2 + … + аn-2х2 + аn-1х + аn

from random import randint

dict_ = {
    0: "\u2070",
    1: "\u00B9",
    2: "\u00B2",
    3: "\u00B3",
    4: "\u2074",
    5: "\u2075",
    6: "\u2076",
    7: "\u2077",
    8: "\u2078",
    9: "\u2079"
}
k = int(input('Введите степень k '))
coef = []
for i in range(k+1):
    coef.append(randint(0, 100))
print(coef)

text = ''
while k > 0:
    if k == 1:
        text = text+str(coef[k])+'x'+" +"
    else:
        text = text+str(coef[k])+'x'+dict_[k]+" +"
    k -= 1

itog = text+str(coef[0])+" = 0"
print(itog)

with open('support33.txt', 'w', encoding='utf_8') as file:
    file.write(itog)
