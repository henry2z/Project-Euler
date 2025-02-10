from common import is_prime

index = 3
length = 1
primes = 0
while True:
    num = index ** 2
    for i in range(3):
        num -= index - 1
        if is_prime(num):
            primes += 1
    length += 4
    if primes / length < 0.1:
        exit(str(index))
    index += 2
