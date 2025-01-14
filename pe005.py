def get_gcd(a, b):
  if a % b == 0:
    return b
  return get_gcd(b, a % b)

def get_lcm(a, b):
  return a * b // get_gcd(a, b)

res = 2
for i in range(3, 21):
  res = get_lcm(i, res)
print(res)