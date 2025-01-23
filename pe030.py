upper_limit = 6 * 9 ** 5
res = 0

for i in range(2, upper_limit + 1):
    num = sum(map(lambda x: int(x) ** 5, list(str(i))))
    if num == i:
        res += i
        print(i)

print(res)