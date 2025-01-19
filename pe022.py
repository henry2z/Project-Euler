f = open("pe022_names.txt")
a = sorted(f.read().split(','))


def score(name, i):
    res = 0
    for letter in name:
        if letter == '"':
            continue
        res += ord(letter) - 64
    res *= (i+1)
    return res


s = 0
for i in range(len(a)):
    s += score(a[i], i)
print(s)
