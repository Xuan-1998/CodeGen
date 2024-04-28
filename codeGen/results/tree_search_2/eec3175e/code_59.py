def subset_sum_divisible_by_m(n, m):
    # Create a boolean array to keep track of whether the cumulative sum
    # is divisible by m at any given point.
    dp = [False] * (m + 1)
    dp[0] = True

    for num in range(1, n+1):
        for i in range(m, -1, -1):
            if i >= num:
                dp[i] |= dp[i-num]

    return dp[m]
