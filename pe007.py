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


def find_prime(n):
  i = 2
  idx = 0
  while True:
    if is_prime_number(i):
      idx += 1
    if idx == n:
      return i
    i += 1


print(find_prime(10001))  