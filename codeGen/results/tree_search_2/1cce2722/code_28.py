def max_points_to_earn(n, sequence):
    dp = {0: n}  # base case: all elements are non-deleted

    for i in range(1, n):
        if sequence[i] != sequence[i-1] or sequence[i-1] != sequence[i-2]:
            dp[i] = min(dp.get(i-1, n), dp.get(i-2, n)) + 1
        else:
            dp[i] = dp[i-1]

    return dp[n-1]
