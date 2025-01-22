from common import is_prime_number
max_res = 0
product = 0
for a in range(-999, 999):
    for b in range(-1000, 1000):
        n = 0
        while is_prime_number(abs(n ** 2 + a * n + b)):
            n += 1
        if max_res < n:
            max_res = n
            product = a * b
print(product)