from common import is_triangle
from math import sqrt


def is_pentagonal(n):
    a = (1 + sqrt(1 + 24 * n)) / 6
    return a.is_integer()


n = 144
while True:
    a = n * (2 * n - 1)
    if is_triangle(a) and is_pentagonal(a):
        exit(str(a))
    n += 1