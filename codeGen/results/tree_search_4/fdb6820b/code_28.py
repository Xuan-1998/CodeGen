import sys
from functools import lru_cache

@lru_cache(maxsize=None)
def dp(i):
    if i < 0:
        return 0
    if i == 0:
        return 1
    res = 0
    for a in arr:
        if i >= a:
            res += dp(i - a)
    return res % (10**9 + 7)

m, n = map(int, input().split())
arr = list(map(int, input().split()))
print(dp(n))
