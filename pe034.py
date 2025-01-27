from math import factorial

memo = {0: 1, 1: 1, 2: 2, 3: 6, 4: 24, 5: 120, 6: 720, 7: 5040, 8: 40320, 9: 362880}

res = 0
for i in range(3, 10000000):
    digits = str(i)
    temp = 0
    for digit in digits:
        temp += memo[int(digit)]
    if temp == i:
        res += i
print(res)