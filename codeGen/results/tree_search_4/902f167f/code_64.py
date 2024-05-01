import sys
from functools import lru_cache

def min_squares(n, m):
    @lru_cache(None)
    def dp(i, j):
        if i == 0 or j == 0:
            return 0
        if i > n or j > m:
            return -1
        res = float('inf')
        for k in range(1, min(i, j) + 1):
            res = min(res, dp(i-k, j) + dp(k-1, k-1) + 1)
        return res

    return dp(n, m)

n, m = map(int, input().split())
print(min_squares(n, m))
