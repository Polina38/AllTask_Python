# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат

def chek(x, y, z):

    print('X={} Y={} Z={}'.format(x, y, z))
    itog1 = not(x or y or z)
    print('выражение в левой части {}'.format(itog1))
    itog2 = (not x) and (not y) and (not z)
    print('выражение в правой части {}'.format(itog2))
    if (itog1 == itog2):
        print('Утверждение истинно')
    else:
        print('Утверждение ложно')


for a in range(0, 2):
    for b in range(0, 2):
        for c in range(0, 2):
            chek(a, b, c)


