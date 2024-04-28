def can_subset_sum_divisible_by_m(set, m):
    n = len(set)
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    # Base case: empty subset has sum 0, which is always divisible by m
    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(m + 1):
            if set[i - 1] <= j:
                dp[i][j] = (dp[i - 1][j - set[i - 1]] or dp[i - 1][j]) and (j % m == 0)
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][m]
