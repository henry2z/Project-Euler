from math import sqrt


def is_pentagonal(n):
    a = (1 + sqrt(1 + 24 * n)) / 6
    return a.is_integer()


N = 5000

for j in range(1, N  + 1):
    for k in range(1, N - j + 1):
        a = (3 * (j ** 2 + k ** 2) - (j + k)) / 2
        b = abs((3 * (j ** 2 - k ** 2) - (j - k)) / 2)
        if is_pentagonal(a) and is_pentagonal(b):
            print(j, k, a, b)
