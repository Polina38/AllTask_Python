# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# входные и выходные данные хранятся в отдельных текстовых файлах
# 12W1B12W3B24W1B14W

with open('support42.txt', 'r') as data:
    data1 = data.read()

str1 = ' '
count = 0
temp = 0
for i in range(len(data1)+1):

    if i == len(data1):
        str1 = str1+str(temp)+data1[count]
    elif data1[i] == data1[count]:
        temp += 1
    else:
        str1 = str1+str(temp)+data1[count]
        count += temp
        i+=count
        temp = 1

print(str1)
with open('support42itog.txt', 'w') as data2:
    data2.write(str1)
