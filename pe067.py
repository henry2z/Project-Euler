f = open('pe067_triangle.txt')
triangle = f.read()

tri_arr = []
for row in triangle.strip().split('\n'):
    tri_arr.append(list(int(num) for num in row.split()))


def max_route(m=0, n=0, memo={}):
    if m == len(tri_arr) - 1:
        return tri_arr[m][n]

    if memo.get((m, n)) is None:
        if memo.get((m + 1, n)) is None:
            memo[(m + 1, n)] = max_route(m + 1, n, memo)
        left = memo[(m + 1, n)]

        if memo.get((m + 1, n + 1)) is None:
            memo[(m + 1, n + 1)] = max_route(m + 1, n + 1, memo)
        right = memo[(m + 1, n + 1)]

        memo[(m, n)] = tri_arr[m][n] + (left if left > right else right)

    return memo[(m, n)]


print(max_route())
