def subset_sum_divisible(n, m):
    # Initialize a list to store previously computed sums
    dp = [False] * (m + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(m, -1, -1):
            if j >= i:
                dp[j] |= dp[j - i]

    return dp[m]
