from math import sqrt


def get_prime_numbers(n):
    num_list = [True for i in range(n + 1)]
    num_list[0] = num_list[1] = False

    for i in range(2, int(sqrt(n)) + 1):
        if num_list[i]:
            for j in range(i * i, n + 1, i):
                num_list[j] = False

    prime_numbers = []
    for i in range(2, n + 1):
        if num_list[i]:
            prime_numbers.append(i)
    return prime_numbers


print(sum(get_prime_numbers(2000000)))
