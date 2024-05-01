dp = [[0] * (N + 1) for _ in range(m + 1)]
for i in range(1, m + 1):
    dp[i][0] = 1
for j in range(1, N + 1):
    for k in range(1, min(j, m) + 1):
        dp[k][j] = (dp[k][j - 1] + dp[k - 1][j]) if k > 0 else 1

print(dp[m][N] % (10**9 + 7))
