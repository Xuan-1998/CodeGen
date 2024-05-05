import sys
from functools import lru_cache

# Read input
t, l, r = map(int, input().split())

@lru_cache(None)
def f(n):
    if n <= 2:
        return n - 1
    dp = [0] * (n + 1)
    for i in range(3, n + 1):
        dp[i] = min(dp[j] + j == i - 1 for j in range(i))
    return dp[n]

result = 0
if t > 0:
    result = sum(ti * f(i) for ti, i in zip(map(int, input().split()), range(l, r + 1))) - l * f(r)
else:
    result = sum(t0 * f(i) for i in range(l, r + 1))

print(result % (10**9 + 7))
