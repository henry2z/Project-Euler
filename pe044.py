from math import sqrt
from common import is_pentagonal

N = 5000

for j in range(1, N  + 1):
    for k in range(1, N - j + 1):
        a = (3 * (j ** 2 + k ** 2) - (j + k)) / 2
        b = abs((3 * (j ** 2 - k ** 2) - (j - k)) / 2)
        if is_pentagonal(a) and is_pentagonal(b):
            print(j, k, a, b)
