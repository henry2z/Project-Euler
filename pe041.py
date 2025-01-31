from itertools import permutations
from math import factorial
from common import is_prime


# ******* Solution 1 *******
res = 0
for i in range(9, 0, -1):
    pandigitals = permutations(range(1, i + 1))
    for j in range(factorial(i)):
        a = int(''.join(map(str, next(pandigitals))))
        if is_prime(a):
            if a > res:
                res = a
    if res != 0:
        break
print(res)


# ******* Solution 2 *******
# def solution(lst, res=[]):
#     if lst == []:
#         n = ''.join(res)
#         if is_prime(int(n)):
#           exit(n)
#     else:
#         for i, item in enumerate(lst):
#             solution(lst[:i]+lst[i+1:], res + [item])
#     return


# for i in range(9, 0, -1):
#     solution([str(x) for x in range(i, 0, -1)])