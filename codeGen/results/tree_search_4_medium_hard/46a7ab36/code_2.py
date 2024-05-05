dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    if i % 2 == 0:
        dp[i][0] = 1
    else:
        for j in range(1, m + 1):
            dp[i][j] += dp[(i // 2) - (i % 2)][j - 1]
            if i > n // 2:
                dp[i][j] += dp[i - 1][j]
dp[m].sort()
print(sum(1 << x) for x in enumerate(dp[m]) if x[1])
