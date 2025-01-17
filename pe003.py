from math import sqrt

a = 600851475143


def is_prime_number(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def largest_prime_factor_slow(n):
    temp = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            temp.append(i)
            if is_prime_number(n // i):
                return n // i

    if sqrt(n) == int(sqrt(n)):
        temp.pop()
    temp.reverse()
    for n in temp:
        if is_prime_number(n):
            return n


def largest_prime_factor_minus(n):
    i = 2
    while True:
        if n % i == 0:
            n //= i
        else:
            if n == 1:
                return i
            i += 1


def largest_prime_factor(n):
    if n < 2:
        return None

    while n % 2 == 0:
        n //= 2
    if n == 1:
        return 2

    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            n //= i
        else:
            i += 2
    return n


for i in range(10001, 100000):
    largest_prime_factor_slow(i)
