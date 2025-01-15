
for a in range(1, 334):
  b = a
  while True:
    c = 1000 - a - b
    if a ** 2 + b ** 2 == c ** 2:
      exit(f'{a * b * c}')
    if a ** 2 + b ** 2 > c ** 2:
      break
    b += 1
