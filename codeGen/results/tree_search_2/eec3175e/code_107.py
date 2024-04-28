def has_subset_sum_divisible_by_m(n, m, set):
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(m + 1):
            if j == 0:
                dp[i][j] = True
            elif set[i - 1] <= j and (set[i - 1] % m == 0 or dp[i - 1][j - set[i - 1]]):
                dp[i][j] = True
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][m]
