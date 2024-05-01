import sys

n, m = map(int, input().split())
dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

# Base case: no squares needed to tile a 0x0 rectangle
dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i >= j:
            dp[i][j] = min(dp[i - j][j], dp[i][j - j] + 1)
        else:
            dp[i][j] = min(dp[i][j - 1], dp[i - 1][j] + 1)

print(dp[n][m])
