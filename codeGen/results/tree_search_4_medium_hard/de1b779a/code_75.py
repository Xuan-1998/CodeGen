import sys
from functools import lru_cache

n, m, c0, d0 = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(m):
    a, b, c, d = map(int, input().split())
    dp[0][i+1] = max(0, d)

@lru_cache(None)
def solve(i, j):
    if i < 0:
        return 0
    if j < 0:
        return d0
    if dp[i][j] > 0:
        return dp[i][j]
    take_stuffing = solve(i - c, j - 1) + d
    not_take_stuffing = solve(i - c0, 0) or d0
    dp[i][j] = max(take_stuffing, not_take_stuffing)
    return dp[i][j]

print(solve(n, m))
