# from itertools import permutations
# a = permutations(range(10))
# for i in range(1000000 - 1):
#     next(a)
# print(next(a))


def permutation(lst, res=[]):
    if lst == []:
        print(res)
    else:
        for i, item in enumerate(lst):
            permutation(lst[:i]+lst[i+1:], res + [item])
    return


def permutation_count(lst, res=[], memo={'count': 0}):
    if lst == []:
        memo['count'] += 1
        if memo['count'] == 1000000:
            exit(res)
    else:
        for i, item in enumerate(lst):
            permutation_count(lst[:i]+lst[i+1:], res + [item], memo)
    return


def permutation_gen(lst, res=[]):
    if lst == []:
        yield res
    else:
        for i, item in enumerate(lst):
            yield from permutation_gen(lst[:i]+lst[i+1:], res + [item])
    return


class IterPermutation:
    def __init__(self, lst):
        self.stack = [(lst, [])]


    def __iter__(self):
        return self
    
    
    def __next__(self):
        while self.stack:
            lst, res = self.stack.pop()
            if lst == []:
                return res
            for i in range(len(lst) - 1, -1, -1):
                self.stack.append((lst[:i] + lst[i+1:], res + [lst[i]]))
        raise StopIteration()


# a = list(range(10))
# perm = permutation_gen(a)
# for i in range(999999):
#     next(perm)
# print(next(perm))

perm = IterPermutation(list(range(4)))
for p in perm:
    print(p)
print(next(perm))
