l = [1, 2]
res = 2

while True:
  n = l[-1] + l[-2]
  if n <= 4000000:
    l.append(n)
    if n % 2 == 0:
      res += n
  else:
    break

print(res)