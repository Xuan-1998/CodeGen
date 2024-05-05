import sys
from functools import lru_cache

@lru_cache(None)
def dp(i, j):
    if i < 0 or j < 0:
        return 0
    elif i == 0 and j == 0:
        return d0
    elif i >= c0 and ai[j-1] >= bi:
        return max(dp(i-ci[j-1], j) + di[j-1], dp(i, j-1))
    else:
        return dp(i-c0, j-1) + d0

n, m, c0, d0 = map(int, input().split())
ai = []
bi = []
ci = []
di = []

for _ in range(m):
    a, b, c, d = map(int, input().split())
    ai.append(a)
    bi.append(b)
    ci.append(c)
    di.append(d)

print(dp(n, m))
