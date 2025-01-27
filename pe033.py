from common import simplify

fractions = []
for den in range(11, 100):
    if den % 10 == 0:
        continue
    str_den = str(den)
    for num in range(11, den):
        if num % 10 == 0:
            continue
        str_num = str(num)
        for char in str_den:
            if char in str_num:
                if int(str_num.replace(char, '', 1)) / int(str_den.replace(char, '', 1)) == num / den:
                    fractions.append((num, den))
                break

numerator = 1
denominator = 1
for fraction in fractions:
    numerator *= fraction[0]
    denominator *= fraction[1]

res = simplify(numerator, denominator)[1]
        
print(res)
