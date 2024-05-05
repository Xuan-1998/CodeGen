from sys import stdin

n, m, c0, d0 = map(int, stdin.readline().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(m + 1):
    dp[0][i] = max(0, d0)

for j in range(m + 1):
    dp[c0][j] = max(dp[c0 - c0][j], d0)

for i in range(c0 + 1, n + 1):
    for j in range(m + 1):
        if j == 0:
            dp[i][j] = max(dp[i - c0][j], d0)
        else:
            dp[i][j] = max(dp[i - ci[k]][k] + di[k] for k in range(j)) or dp[i][j]

print(max(0, dp[n][m]))
