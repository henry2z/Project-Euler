from itertools import combinations, permutations
from common import is_prime

res = []
for i in range(1000, 10000):
    perm = [int(''.join(x)) for x in list(permutations(str(i)))]
    primes = []

    for num in perm:
        if is_prime(num):
            primes.append(num)

    comb = list(combinations(primes, 3))
    
    for t in comb:
        if (len(str(t[0])) == 4 and len(str(t[1])) == 4 and len(str(t[2])) == 4) and \
           not (t[0] == t[1] or t[0] == t[2] or t[1] == t[2]) and \
           (t[2] > t[1] and t[1] > t[0]) and \
           (t[1] - t[0] == t[2] - t[1]) and \
           (t not in res):
            res.append(t)

print(res)