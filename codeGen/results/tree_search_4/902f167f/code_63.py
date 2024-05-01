import sys

n, m = map(int, input().split())

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        min_squares = float('inf')
        for k in range(1, min(i, j) + 1):
            min_squares = min(min_squares, dp[i-k][j] + dp[k-1][k])
        dp[i][j] = 1 + min_squares

print(dp[n][m])
