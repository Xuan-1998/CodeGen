from collections import defaultdict

n = int(input())
sequence = list(map(int, input().split()))

def f(x, y):
    if x <= 0 or x > n:
        return -1
    memo = {}
    while True:
        if (x, y) in memo:
            return memo[(x, y)]
        memo[(x, y)] = y
        x += sequence[x]
        y += sequence[x]
        x -= sequence[x]
        y += sequence[x]
    return -1

for i in range(2, n + 1):
    print(f(i, 0))
