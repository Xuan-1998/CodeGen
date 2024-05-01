===BEGIN CODE===
n, m = map(int, input().split())
dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    dp[i][0] = dp[i - 1][0] + 1
    for j in range(1, m + 1):
        if j <= i and (j == 1 or i == 1):
            dp[i][j] = min(dp[i][j], 1)
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

print(min(dp[-1][-1], dp[-2][-1]))
