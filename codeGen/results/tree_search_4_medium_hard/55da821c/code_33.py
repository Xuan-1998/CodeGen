import sys

n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    s_i, x_i = map(int, input().split())
    for j in range(1, min(i + 1, m + 1)):
        if s_i == j:
            dp[i][j] = dp[x_i - 1][j]
        else:
            dp[i][j] = min(dp[x_i - 1][k] for k in range(j)) + 1

print(dp[n][m])
