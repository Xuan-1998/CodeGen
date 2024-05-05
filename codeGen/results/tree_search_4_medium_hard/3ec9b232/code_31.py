from functools import lru_cache
import sys

n = int(input())
m = list(map(int, input().split()))
mod = 10**9 + 7

@lru_cache(None)
def dp(i, j):
    if j < i:
        return 0
    if i == n - 1:
        return 1 if m[i] == j else 0
    res = sum(dp(k, j-1) * (m[k] == m[i]) for k in range(i+1))
    return res % mod

print((dp(0, n-1)) % mod)
