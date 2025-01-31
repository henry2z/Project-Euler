from math import sqrt


def is_prime(n):
    '''Checks if a number is prime.'''
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


def get_factors(n, proper=False):
    '''Get all factors in a number.'''
    factors_front = []
    factors_behind = []

    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            factors_front.append(i)
            factors_behind.append(n // i)
    if factors_front[-1] == factors_behind[-1]:
        factors_behind.pop()
    factors_behind.reverse()
    if proper:
        factors_behind.pop()
    return factors_front + factors_behind


def is_unique(s):
    '''Returns True if a string is unique, returns False if isn't.'''
    lst = []
    for char in s:
        if char in lst:
            return False
        lst.append(char)
    return True


def simplify(numerator, denominator):
    '''Simplify a fraction.'''
    gcd = get_gcd(numerator, denominator)
    return numerator // gcd, denominator // gcd


def get_gcd(a, b):
    '''Get the greatest common divisor of the variables a and b'''
    if a % b == 0:
        return b
    return get_gcd(b, a % b)


def get_lcm(a, b):
    '''Get the least common multiple of the variables a and b'''
    return a * b // get_gcd(a, b)


def is_pandigital(n, a, b):
    '''Calculates if n is a through b pandigital'''
    if sorted(str(n)) == sorted(''.join([str(num) for num in list(range(a, b + 1))])):
        return True
    return False


def get_primes(n):
    '''Gets all primes from 1 to n'''
    num_list = [True for i in range(n + 1)]
    num_list[0] = num_list[1] = False
    
    for i in range(2, int(sqrt(n)) + 1):
        if num_list[i]:
            for j in range(i * i, n + 1, i):
                num_list[j] = False

    prime_numbers = []
    for i in range(2, n + 1):
        if num_list[i]:
            prime_numbers.append(i)
    return prime_numbers


def is_triangle(n):
    a = (-1 + sqrt(1 + 8 * n)) / 2
    if int(a) == a:
        return True
    return False