n, m, c0, d0 = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for j in range(m + 1):
    if j == 0:
        dp[0][j] = max(dp[0][j], c0)
    else:
        for i in range(n + 1):
            if j > 0:
                dp[i][j] = max(dp[max(0, i - ci[j])][j - 1], dp[i][j - 1]) + di[j]
            else:
                dp[i][j] = max(dp[i - 1][j], c0)

print(dp[n][m])
