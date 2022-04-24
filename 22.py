# Найти сумму чисел списка стоящих на нечетной позиции

my_spisok = [12, 87, 9, 53, 21, 4, 62, 35]
summ = 0
for item in range(len(my_spisok)):
    if (item % 2 != 0):
        summ = summ+my_spisok[item]

print(summ)
