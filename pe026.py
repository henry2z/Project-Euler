def cycle_len(divisor):
    remainders = []
    dividend = 1
    while True:
        while dividend < divisor:
            dividend *= 10
        remainder = dividend % divisor
        if remainder in remainders:
            return len(remainders)
        if remainder == 0:
            return 0
        remainders.append(remainder)
        dividend = remainder


max_len = 0
max_res = 0
for i in range(200000, 200050):
    res = cycle_len(i)
    if res > max_len:
        max_len = res
        max_res = i
print(max_len, max_res)
