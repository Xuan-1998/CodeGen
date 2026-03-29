for i in range(2, n + 1):
    dp[i] = min(dp[i-1], a[i-1] - s) + a[i-1]
