N = 1001
arr = [[0 for m in range(N)] for n in range(N)]
i = j = N // 2
num = 1
steps = 1
arr[i][j] = 1
direction = 1

try: 
    while True:
        for n in range(steps):
            num += 1
            j += direction
            arr[i][j] = num
            
        for n in range(steps):
            num += 1
            i += direction
            arr[i][j] = num
        steps += 1
        direction *= -1
except IndexError:
    pass

res = 0
for n in range(N):
    res += arr[n][n]
    
for n in range(N):
    res += arr[n][N - 1 - n]

res -= 1
print(res)