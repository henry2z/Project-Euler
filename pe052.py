from common import same_characters

i = 100000
while True:
    if same_characters(i, i * 2, i * 3, i * 4, i * 5, i * 6):
        exit(str(i))
    i += 1
