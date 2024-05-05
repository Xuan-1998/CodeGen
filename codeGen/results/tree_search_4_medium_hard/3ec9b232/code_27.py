import sys
from functools import lru_cache

@lru_cache(None)
def dp(i, j):
    if i > j:
        return 0
    if i == 0:
        return 1
    res = 0
    for k in range(j+1):
        if M[k] < M[i-1]:
            res += dp(i-1, k)
    return res

n = int(input())
M = list(map(int, input().split()))
print(dp(n-1, n-2) % (10**9 + 7))
