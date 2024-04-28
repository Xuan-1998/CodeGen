n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = min((i - 1) * dp[i-1][j] // (i) + (j - 1) * dp[i][j-1] // (j), 1)
print(dp[-1][-1])
