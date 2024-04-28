def max_points(a):
    n = len(a)
    dp = [0] * (n + 1)

    for s in range(2, n + 1):
        if a[s - 1] % 2 == 1:
            dp[s] = max(dp[s-2] + s if s >= 2 else 0, dp[s-1] + 1)
        else:
            dp[s] = max(dp[s-2] + s if s >= 2 else 0, dp[s-1])

    return dp[n]

