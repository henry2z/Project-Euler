from common import is_prime

current = 0
res = 0
terms = []
length = 0
primes = []

for i in range(1000000):
    if sum(primes) + i >= 1000000:
        break
    if is_prime(i):
        primes.append(i)

while True:
    for prime in primes:
        current += prime
        terms.append(prime)
        if is_prime(current) and len(terms) > length:
            res = current
            length = len(terms)
    primes = primes[1:]
    if primes == []:
        break
    terms = []
    current = 0

print(res)