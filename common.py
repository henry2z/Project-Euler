from math import sqrt


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


def get_factors(n, proper=False):
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