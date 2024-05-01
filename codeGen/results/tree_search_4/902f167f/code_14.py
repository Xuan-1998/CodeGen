n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = 1
    for j in range(m + 1):
        dp[0][j] = 1

for k in range(1, min(n, m) + 1):
    for i in range(k, n + 1):
        for j in range(k, m + 1):
            dp[i][j] = min(dp[i-k][j-k] + 1, dp[i][j])

print(dp[n][m])
