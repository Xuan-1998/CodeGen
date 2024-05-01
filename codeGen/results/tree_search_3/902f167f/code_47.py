import sys

n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n + 1):
    if i == 0:
        dp[i][j] = j
    else:
        for j in range(m + 1):
            if j == 0:
                dp[i][j] = i
            elif i > 0 and j > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

print(dp[n][m])
