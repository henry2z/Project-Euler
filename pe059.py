from itertools import product
from re import sub


def decrypt(text, key):
    paragraph = ''
    for i, ascii in enumerate(text):
        paragraph += chr(int(ascii) ^ key[i % 3])
    return paragraph


def get_proportion_of_letters(text):
    return len(sub(r'[a-zA-Z]', '', ''.join(text))) / len(text)


def get_average_word_length(text):
    return sum(map(len, text.split())) / len(text.split())


file = open('pe059_cipher.txt')
encrypted_text = file.read().split(',')
file.close()

asciis_list = product(range(97, 123), repeat=3)

for asciis in asciis_list:
    decrypted_text = decrypt(encrypted_text, asciis)
    word_average_length = get_average_word_length(''.join(decrypted_text))
    if get_proportion_of_letters(decrypted_text) < .3 and word_average_length <= 6:
        print(sum(map(ord, ''.join(decrypted_text))))
