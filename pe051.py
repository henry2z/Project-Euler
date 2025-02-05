from common import is_prime
from itertools import combinations

i = 56004

while True:
    # Look at all the possibilities
    digit_count = len(str(i))
    for count in range(1, digit_count):
        for idx_cb in combinations(range(digit_count), count):
            composite_count = 0
            prime_count = 0
            smallest = None
            start = 0
            if idx_cb[0] == 0:
                start = 1
            for digit in range(start, 10):
                lst = list(str(i))
                for idx in idx_cb:
                    lst[idx] = str(digit)
                num = int(''.join(lst))
                if is_prime(num):
                    prime_count += 1
                    if smallest is None:
                        smallest = num
                else:
                    composite_count += 1
                # See if i is part of the eight-prime value family
                if composite_count == 3:
                    break
                if prime_count == 8:
                    print(i)
                    print(idx_cb)
                    print(f'result: {str(smallest)}')
                    exit()
    i += 1
