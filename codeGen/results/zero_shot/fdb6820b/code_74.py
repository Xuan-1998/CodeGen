import sys
from functools import lru_cache

m, N = map(int, input().split())
dp = [[0]*(N+1) for _ in range(m+1)]

for i in range(1, m+1):
    a = list(map(int, input().split()))
    for j in range(N+1):
        dp[i][j] = (dp[i-1][j] + 1 if j >= a[0] else dp[i-1][j]) % (10**9 + 7)

print(dp[m][N])
