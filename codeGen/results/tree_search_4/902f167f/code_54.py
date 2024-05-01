import sys

n, m = map(int, input().split())
dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][1] = 1
for j in range(1, m+1):
    dp[1][j] = 1

for i in range(2, n+1):
    for j in range(2, m+1):
        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
        if i == 1 or j == 1:
            dp[i][j] = max(i, j)

print(dp[n][m])
