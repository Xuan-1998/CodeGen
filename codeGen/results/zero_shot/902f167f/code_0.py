n, m = map(int, input().split())
dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
dp[0] = [0] * (m + 1)
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i >= j:
            dp[i][j] = min(dp[i][j], dp[i - j][j] + 1)
print(min(dp[n]))
