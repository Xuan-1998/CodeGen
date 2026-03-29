import sys
from functools import lru_cache

@lru_cache(None)
def dp(i, j):
    if i == 0:
        return d0
    if j < ci[i-1]:
        return dp(i-1, j)
    return max(dp(i-1, j), dp(i, j-ci[i-1])+di[i-1])

n, m, c0, d0 = map(int, sys.stdin.readline().split())
ci, di = [], []
for _ in range(m):
    a, b, c, d = map(int, sys.stdin.readline().split())
    ci.append(c)
    di.append(d)

print(dp(m, n))
