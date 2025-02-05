from math import comb

s = 0
for n in range(1, 101):
    for r in range(1, n + 1):
        if comb(n, r) > 1000000:
            s += 1
print(s)