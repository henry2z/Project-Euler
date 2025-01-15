temp = 0
res = 0

for i in range(1, 101):
  temp += i**2

for i in range(1, 101):
  res += i
res **= 2
res -= temp
print(res)