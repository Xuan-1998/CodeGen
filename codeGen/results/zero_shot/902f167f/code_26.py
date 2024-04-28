n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i <= 3 and j <= 3:
            dp[i][j] = min(i, j)
        else:
            dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])
print(dp[n][m])
