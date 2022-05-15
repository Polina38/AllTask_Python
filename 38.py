# Напишите программу, удаляющую из текста все слова содержащие "абв".



str= 'страбв евеве абвщззз абв тфабвж'
str= str.split()
print(str)

str1=' '
for i in str:
    if 'абв' not in i:
        str1= str1+i+' '
print(str1)