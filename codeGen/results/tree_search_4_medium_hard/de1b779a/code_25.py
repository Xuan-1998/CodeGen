import sys
from functools import lru_cache

n, m, c0, d0 = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
dp[0][0] = d0

@lru_cache(None)
def dp(i, j):
    if i < 0 or j < 0:
        return 0
    if j == 0:  # no stuffing type used
        return max(dp(i - c0, 0), 0) * d0
    if i >= c0 and j > 0:
        return max(dp(i - c0, 0), dp(i - ci[j-1], j-1)) + di[j-1]
    return 0

print(max(0, dp(n, m)))
