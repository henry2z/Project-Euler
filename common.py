from math import sqrt


def is_prime_number(n):
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


class IterPermutation:
    '''Self made permutation. You can also import from Itertools.'''
    def __init__(self, lst):
        self.stack = [(lst, [])]


    def __iter__(self):
        return self
    
    
    def __next__(self):
        while self.stack:
            lst, res = self.stack.pop()
            if lst == []:
                return res
            for i in range(len(lst) - 1, -1, -1):
                self.stack.append((lst[:i] + lst[i+1:], res + [lst[i]]))
        raise StopIteration()


def is_unique(s):
    '''Returns True if a string is unique, returns False if isn't.'''
    lst = []
    for char in s:
        if char in lst:
            return False
        lst.append(char)
    return True