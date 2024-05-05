import math
from functools import lru_cache

n = int(input())
M = list(map(int, input().split()))
@lru_cache(None)
def dp(i, j):
    if i == 0:
        return 1
    if j < 0 or M[j] != i+1:
        return 0
    return (dp(i-1, j) + dp(i-1, j-1)) % (10**9+7)

print(dp(n-1, n-1))
