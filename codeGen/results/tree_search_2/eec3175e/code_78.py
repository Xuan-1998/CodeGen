from collections import defaultdict

def subset_sum(n, m):
    dp = defaultdict(int)
    for x in range(n):
        s = 0
        for y in range(x, n):
            s += [y]
        if s % m == 0:
            return 1
    return 0

n, m = map(int, input().split())
print(subset_sum(n, m))
