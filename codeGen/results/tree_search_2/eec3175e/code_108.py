def can_sum_subset(set_, m):
    n = len(set_)
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if set_[i - 1] <= j:
                dp[i][j] = (dp[i - 1][j] or dp[i - 1][j - set_[i - 1]])
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][m]
