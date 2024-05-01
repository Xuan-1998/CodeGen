import sys

n, m = map(int, input().split())

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i == 1 and j == 1:
            dp[i][j] = 1
        else:
            min_squares = float('inf')
            for k in range(min(i, j) ** 0.5 + 1):
                if i - k * k >= 1 and j - k * k >= 1:
                    min_squares = min(min_squares, dp[i - k * k][j - k * k] + (i - k * k) * (j - k * k))
            dp[i][j] = min_squares

print(dp[n][m])
