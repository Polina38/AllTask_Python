# Реализовать алгоритм перемешивания списка.


import random

list = [2, 18, 7, 34, 61, 8, 50]
# random.shuffle(list)

for i in range(len(list)):
    temp = list[i]
    el = random.choice(list)
    k = list.index(el)
    list[i] = el
    list[k] = temp

print(list)
