n, m = map(int, input().split())
dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
dp[0] = dp[:, 0] = [0]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i % 2 == 1:
            dp[i][j] = min(dp[i][j], dp[i - 1][j])
        else:
            dp[i][j] = min(dp[i][j], dp[i // 2][j // 2] + (i // 2) * (j // 2))
print(min(dp[-1]))
