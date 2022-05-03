# Составить список простых множителей натурального числа N


n = int(input('Введите число N '))
list = []
i = 2
while i <= n:
    if n % i == 0:
        list.append(i)
        while n % i == 0:
            n = n//i
    else:
        i += 1
print('список простых множителей заданного числа ',list)
