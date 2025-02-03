from common import is_prime
from math import sqrt

i = 3
primes = []
while True:
    if is_prime(i):
        primes.append(i)
        i += 2
        continue
    flag = True
    for prime in primes:
        left = i - prime
        if (int(sqrt(left / 2)) == sqrt(left / 2)):
            flag = False
    if flag:
        exit(str(i))
    i += 2