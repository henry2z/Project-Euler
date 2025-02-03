from common import prime_factorization

i = 1

while True:
    flag = True
    for n in range(i, i + 4):
        if not len(set(prime_factorization(n))) == 4:
            flag = False
    if flag:
        exit(str(i))
    i += 1
