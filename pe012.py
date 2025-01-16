from math import sqrt


def get_factors(n):
  factors_front = []
  factors_behind = []
  for i in range(1, int(sqrt(n)) + 1):
      if n % i == 0:
          factors_front.append(i)
          factors_behind.append(n // i)
  if factors_front[-1] == factors_behind[-1]:
      factors_behind.pop()
  factors_behind.reverse()
  return factors_front + factors_behind


def solution(count):
  n = 1
  while True:
    res = n * (n + 1) // 2
    if len(get_factors(res)) >= count:
      return res
    n += 1

print(solution(500))