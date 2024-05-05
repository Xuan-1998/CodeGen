import sys
from functools import lru_cache

@lru_cache(None)
def dp(i, j):
    if i < 1 or j < 0:
        return 0
    if j > k:
        return dp(i-1, j-1) + arr[i]
    if i - j - 1 >= z and j > 0:
        return max(dp(i-1, j-1) + arr[i], dp(i-1, j-2) + arr[i-1])
    return dp(i-1, j-1) + arr[i]

t = int(input())
for _ in range(t):
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    print(dp(n, k))
