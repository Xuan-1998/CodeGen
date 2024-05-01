def max_points_earned(a):
    n = len(a)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if a[i - 1] == a[i - 2] + 1 or a[i - 1] == a[i - 2] - 1:
            dp[i] = max(dp[i - 1], dp[i - 2])
        else:
            dp[i] = max(dp[i - 1], dp[i - 2]) + 1

    return dp[-1]
