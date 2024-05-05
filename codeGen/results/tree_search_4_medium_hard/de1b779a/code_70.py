n, m, c0, d0 = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = max(dp[i-1][0], d0)

for j in range(1, m + 1):
    ai, bi, ci, di = map(int, input().split())
    for i in range(n, c0 - 1, -1):
        if ci < i:
            dp[i][j] = max(dp[i-1][0], dp[c0][0])
        else:
            dp[i][j] = max(dp[i-ci][j-1] + di, dp[i-1][0])

print(max(0, dp[n][m]))
