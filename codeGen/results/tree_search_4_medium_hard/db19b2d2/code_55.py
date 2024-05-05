import sys
from functools import lru_cache

# Read input from stdin
n, m, h = map(int, input().split())
s = list(map(int, input().split()))

@lru_cache(None)
def dp(k):
    if k == n:
        return 1 if sum(s) - s[h-1] >= n - k else 0
    return max(0, dp(k-1)) + (s[h-1] / sum(s)) * dp(k-1)

print(dp(n))
