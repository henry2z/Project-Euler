
max_times = 0
res = 0

for i in range(1, 1000000):
  times = 0
  n = i
  while n != 1:
    if n % 2 == 0:
      n //= 2
    else:
      n = 3 * n + 1
    times += 1
  if times > max_times:
    max_times = times
    res = i

print(res)
