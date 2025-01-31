from common import is_triangle

f = open("pe042_words.txt")
a = sorted(f.read().split(','))


def score(word):
    res = 0
    for letter in word:
        if letter == '"':
            continue
        res += ord(letter) - 64
    return res


s = 0
l = []
for i in range(len(a)):
    if is_triangle(score(a[i])):
        s += 1
        l.append(a[i])
print(s)

# print(score('"ABLE"'))