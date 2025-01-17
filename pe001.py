n = 0
l = []
for i in range(1, 1000):
    if i % 3 == 0:
        n += i
        l.append(i)
    if i % 5 == 0 and i not in l:
        n += i
print(n)
