# Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её.

matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print('{}\n{}\n{}'.format(matrix[:3], matrix[3:6], matrix[6:]))
symbol1 = 'x'
symbol2 = '0'


def Stop_game(list):
    terms1 = matrix[0] == matrix[1] == matrix[2]
    terms2 = matrix[3] == matrix[4] == matrix[5]
    terms3 = matrix[6] == matrix[7] == matrix[8]
    terms4 = matrix[0] == matrix[3] == matrix[6]
    terms5 = matrix[1] == matrix[4] == matrix[7]
    terms6 = matrix[2] == matrix[5] == matrix[8]
    terms7 = matrix[0] == matrix[4] == matrix[8]
    terms8 = matrix[2] == matrix[4] == matrix[6]
    list_new = [terms1, terms2, terms3, terms4, terms5, terms6, terms7, terms8]
    return (any(list_new))


k = 1
while k < 9:
    step1 = int(input('Первый игрок- играем х: введите номер ячейки '))
    matrix[step1-1] = symbol1
    print('{}\n{}\n{}'.format(matrix[:3], matrix[3:6], matrix[6:]))
    k += 1
    if k >= 4 and Stop_game(matrix) == True:
        print('Победа первого игрока!')
        break
    step2 = int(input('Второй игрок- играем 0: введите номер ячейки '))
    matrix[step2-1] = symbol2
    print('{}\n{}\n{}'.format(matrix[:3], matrix[3:6], matrix[6:]))
    k += 1
    if k >= 4 and Stop_game(matrix) == True:
        print('Победа второго игрока!')
        break

if k >= 9:
    print('Ничья! Играем вновь! ')
