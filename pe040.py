s = ''
a = 1
res = 1
while len(s) < 1000000:
    s += str(a)
    a += 1

for i in range(6):
    res *= int(s[10 ** i - 1])

print(res)