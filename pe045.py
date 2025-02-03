from common import is_triangle, is_pentagonal

n = 144
while True:
    a = n * (2 * n - 1)
    if is_triangle(a) and is_pentagonal(a):
        exit(str(a))
    n += 1