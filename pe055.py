from common import is_palindromic


def is_lychrel(n):
    for i in range(50):
        n += int(str(n)[::-1])
        if is_palindromic(n):
            return False
    return True


res = 0
for i in range(1, 10000):
    if is_lychrel(i):
        res += 1
print(res)
