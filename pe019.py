MONTH_DATES = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    return False


def is_sunday(year, month):
    res = 0
    for i in range(1900, year):
        if is_leap(i):
            res += 1
        res += 365

    for i in range(month - 1):
        if i == 1 and is_leap(year):
            res += 1
        res += MONTH_DATES[i]

    if res % 7 == 6:
        return True
    return False


num = 0
for i in range(1901, 2001):
    for j in range(1, 13):
        if is_sunday(i, j):
            num += 1
print(num)
