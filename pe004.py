def break_down(n):
    for i in range(999, 99, -1):
        if n % i == 0 and len(str(n // i)) == 3:
            return i, n // i


for i in range(999, 99, -1):
    n = int(str(i) + str(i)[::-1])
    res = break_down(n)
    if res:
        print(f'{n} = {res[0]} x {res[1]}')
        break
