# Реализовать алгоритм задания случайных чисел.
# Без использования встроенного генератора псевдослучайных чисел


import time


def random_number(minimum, maximum):
    now = str(time.time())
    print(now)
    rnd = int(now[::-1][:3:])/1000
    return minimum + rnd*(maximum-minimum)


print(random_number(1, 3))
