a = b = 1
res = 0

for i in range(1000):
    a, b = a + b, 2 * a + b
    if len(str(a)) + 1 == len(str(b)):
        res += 1

print(res)