def max_points(a):
    n = len(a)
    dp = [0] * (n + 2)

    for i in range(1, n + 1):
        if a[i-1] != 0:
            dp[i] = max(dp[i-1], dp[max(0, i-2)])
        else:
            dp[i] = dp[i-1]

    return dp[-1]
