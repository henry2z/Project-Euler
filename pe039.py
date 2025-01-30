from math import sqrt

res = 0
num = 0
for p in range(3, 1001):
    temp = 0
    for a in range(1, p):
        for b in range(1, p - a):
            if a > b:
                continue
            c = sqrt(a ** 2 + b ** 2)
            if a + b + c == p and c == int(c):
                temp += 1
    if temp > num:
        num = temp
        res = p

print(res, num)