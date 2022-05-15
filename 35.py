# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы
# выполнялось условие A[i] - 1 = A[i-1]. Найти его.

with open('support35.txt', 'r') as data:
    data1 = data.read().split()
data1 = list(map(int, data1))
data1.sort()
print(data1)

for i in range(len(data1)-1):
    if data1[i+1] != data1[i]+1:
        print('Потеряное число ', data1[i]+1)
