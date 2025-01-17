ONES = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
TENS = ['', '', 'twenty', 'thirty', 'forty', 'fifty',
        'sixty', 'seventy', 'eighty', 'ninety']


def read_under_thousand(num):
    num = int(num)
    res = ''
    if num >= 100:
        res += ONES[num // 100] + ' hundred'
        num %= 100
        if num != 0:
            res += ' and'
    if num >= 20:
        res += ' ' + TENS[num // 10]
        num %= 10
    res += ' ' + ONES[num]
    return len(res.replace(' ', ''))


num = 0
for i in range(1, 1000):
    num += read_under_thousand(i)
num += len('onethousand')
print(num)
