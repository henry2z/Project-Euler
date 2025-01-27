def is_palindromic(num):
    num = str(num)
    return True if num == num[::-1] else False

res = 0
for i in range(1000000):
    if is_palindromic(i) and is_palindromic(int(bin(i)[2:])):
        res += i
print(res)
