n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i < j:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
        else:
            dp[i][j] = 1
print(min(max(dp[i][m] for i in range(n, m // 2 + 1)), max(dp[n][j] for j in range(m, n // 2 + 1))))
