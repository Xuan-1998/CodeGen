import sys
from functools import lru_cache

m, N = map(int, input().split())
arr = list(map(int, input().split()))

dp = [[0] * (N + 1) for _ in range(m + 1)]
dp[0][0] = 1

for i in range(1, m + 1):
    for j in range(N + 1):
        if arr[i - 1] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = (dp[i][j - arr[i - 1]] or 0) + dp[i - 1][j]

print((dp[m][N] % (10 ** 9 + 7)))
