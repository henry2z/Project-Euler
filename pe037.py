from common import is_prime


def is_truntacable(n):
    n_copy = str(n)
    digits = len(n_copy)
    for i in range(digits):
        if not int(is_prime(int(n_copy))):
            return False
        n_copy = n_copy[:-1]
    n_copy = str(n)
    for i in range(digits):
        if not int(is_prime(int(n_copy))):
            return False
        n_copy = n_copy[1:]
    return True


temp = 10
count = 0
s = 0
while True:
    if is_truntacable(temp):
        count += 1
        s += temp
        print(temp)
    if count == 11:
        break
    temp += 1
print(s)
