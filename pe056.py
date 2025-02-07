
res = 0
for a in range(1, 100):
    for b in range(1, 100):
        c = sum(map(int, list(str(a ** b))))
        if c > res:
            res = c
print(res)
