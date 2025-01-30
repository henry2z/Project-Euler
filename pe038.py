from common import is_pandigital
res = 0
for i in range(1, 10000):
    temp = ''
    j = 1
    while len(temp) < 9:
        temp += str(i * j)
        j += 1
    if len(temp) > 9:
        continue
    if is_pandigital(int(temp), 1, 9) and int(temp) > res:
        res = int(temp)
print(res)