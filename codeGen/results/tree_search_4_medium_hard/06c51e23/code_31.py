import sys
from functools import lru_cache

@lru_cache(maxsize=None)
def solve(i, t):
    if i == 0:
        return 1
    dp = [0] * (i + 1)
    for j in range(10**9):
        if j <= t and (j % 2 == 0 or (dp[i - 1] > 0)):
            if i < n:
                return min(solve(i + 1, j), solve(i, j - 1))
            else:
                return dp[i - 1]
    return 0

n, t = map(int, input().split())
f = float(input())

dp = [0] * (n + 1)
for i in range(n):
    if f < 10**9:
        break
    f *= 10
dp[0] = 1
for i in range(1, n + 1):
    if f >= 10**9:
        dp[i] = min(solve(i, t), solve(i - 1, t - (int(f) - int(f)) * 1000000))
    else:
        dp[i] = min(int(f), dp[i - 1])
print(dp[n].astype(int).sum())
