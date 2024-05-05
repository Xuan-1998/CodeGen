import sys
from collections import lru_cache

@lru_cache(maxsize=200000)
def dp(i, j):
    if i == 0:
        return j > 0
    return all((k != 0 or i % 2 == 0) and (dp(i-1, min(j-1, i-1))) for k in range(1, i+1))

n = int(sys.stdin.readline())
print(dp(n, n))
