def max_points(a):
    n = len(a)
    k_max = 100  # assume at most 105 integers in the input

    dp = [[0] * (k_max + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for k in range(k_max + 1):
            if a[i - 1] == a[k - 1] + 1 or a[i - 1] == a[k - 1] - 1:
                dp[i][k] = max(dp[i - 1][k - 1], dp[i - 1][k])
            else:
                dp[i][k] = dp[i - 1][k]

    return dp[n][k_max]
