from math import factorial
from common import is_prime

def is_circular_prime(num):
    digits = len(str(num))
    rotations = factorial(digits)
    num = str(num)
    for i in range(rotations):
        if not is_prime(int(num)):
            return False
        num = num[1:] + num[0]
    return True

s = 0
for i in range(2, 1000000):
    if is_circular_prime(i):
        s += 1
print(s)