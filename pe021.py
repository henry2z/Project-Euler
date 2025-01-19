from math import sqrt


def d(n):
    factors_front = []
    factors_behind = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            factors_front.append(i)
            factors_behind.append(n // i)
    if factors_front[-1] == factors_behind[-1]:
        factors_behind.pop()
    factors_behind.reverse()
    factors = factors_front + factors_behind
    return sum(factors[:-1])


def is_amicable(a):
    b = d(a)
    if d(b) == a and b != a:
        return True
    return False


res = 0
for i in range(2, 10000):
    if is_amicable(i):
        res += i


print(res)
