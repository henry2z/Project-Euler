from common import get_factors


def is_abundant(a):
    if sum(get_factors(a, True)) > a:
        return True
    return False


abundants = []
res = 0

# PLAN 1
# for i in range(12, 28124):
#     res += i
#     for abundant in abundants:
#         if (i - abundant) in abundants:
#             res -= i
#             break
#     if is_abundant(i):
#         abundants.append(i)
#     print(i)

# PLAN 2
for i in range(12, 28124):
    flag = False
    for abundant in abundants:
        if (i - abundant) in abundants:
            flag = True
            break
    if not flag:
        res += i
        print(i)
    if is_abundant(i):
        abundants.append(i)

print(res + 66)
