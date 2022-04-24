# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д. Пример: [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from xml.dom.minidom import Element


my_spisok = [12, 87, 9, 53, 21, 4, 62, 35]
new_spisok = []

for item in range(int(len(my_spisok)/2)):
    new_spisok.append(my_spisok[item]*my_spisok[len(my_spisok)-1-item])
print(new_spisok)
