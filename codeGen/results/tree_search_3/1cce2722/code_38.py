def max_points(a):
    n = len(a)
    dp = [-float('inf')] * (n + 1)

    for i in range(1, n + 1):
        for k in range(105):
            if a[i - 1] == k:
                dp[i] = max(dp[i], dp[i - 1])
            else:
                dp[i] = max(dp[i], dp[i - 1] + (a[i - 1] != k))

    return max(dp)
