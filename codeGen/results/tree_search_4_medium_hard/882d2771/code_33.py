import sys
from functools import lru_cache

@lru_cache(None)
def f(n):
    if n <= 1:
        return 0
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        dp[i] = min(dp[i - 1] + 1, dp[i - 2] + 2) if i > 1 else 0
    return dp[n]

t, l, r = map(int, input().split())
result = sum(ti * f(l + i - 1) for i in range(t)) - l * f(r)
print(result % (10**9 + 7))
