from sys import stdin

n, m = map(int, stdin.readline().split())

dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i < 2 or j < 2:
            dp[i][j] = 1
        else:
            dp[i][j] = min((dp[i - 1][k] + dp[k][j - 1]) for k in range(min(i, j)) + 1)

print(dp[n][m])
