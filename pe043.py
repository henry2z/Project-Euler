from itertools import permutations
from math import factorial


def solution(n):
    def temp(a, b, c):
        return a * 100 + b * 10 + c
    if temp(n[1], n[2], n[3]) % 2 == 0 and temp(n[2], n[3], n[4]) % 3 == 0 and \
       temp(n[3], n[4], n[5]) % 5 == 0 and temp(n[4], n[5], n[6]) % 7 == 0 and \
       temp(n[4], n[5], n[6]) % 7 == 0 and temp(n[5], n[6], n[7]) % 11 == 0 and \
       temp(n[6], n[7], n[8]) % 13 == 0 and temp(n[7], n[8], n[9]) % 17 == 0:
           return True
    return False


s = 0
pandigitals = permutations(range(10))
for i in range(factorial(10)):
    a = next(pandigitals)
    if solution(list(a)):
        s += int("".join(map(str,  a)))
print(s)