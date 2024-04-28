n, m = map(int, input().split())
dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(1, n + 1):
    dp[i][0] = dp[i - 1][0] + 1
for j in range(1, m + 1):
    dp[0][j] = dp[0][j - 1] + 1
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i >= j:
            dp[i][j] = min(dp[i][j], dp[i - j][j] + 1)
        if j >= i:
            dp[i][j] = min(dp[i][j], dp[i][j - i] + 1)
print(min(max(i // j for i, j in zip(range(n + 1), range(m + 1))), 1))
