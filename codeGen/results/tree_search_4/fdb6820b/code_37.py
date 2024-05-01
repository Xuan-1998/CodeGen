import sys

m, N = map(int, input().split())
arr = list(map(int, input().split()))
mod = 10**9 + 7

dp = [[0] * (N + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(N + 1):
        dp[i][j] = sum(dp[k][j-1] for k in range(i)) if j > 0 else 1

for i in range(1, N + 1):
    for j in range(m, -1, -1):
        dp[j][i] = sum(1 if n-k <= i else dp[k][i-1] for k in range(j+1))

print((dp[m][N] % mod))
