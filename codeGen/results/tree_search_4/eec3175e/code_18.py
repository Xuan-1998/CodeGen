def can_sum_subset(nums, m):
    n = len(nums)
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    # Base case: dp[0][j] = 1 if j == 0, and 0 otherwise.
    for k in range(m + 1):
        dp[0][k] = k == 0

    for i in range(1, n + 1):
        for k in range(m + 1):
            if k <= nums[i - 1]:
                dp[i][k] = dp[i][k] or dp[i - 1][k - nums[i - 1]]
            else:
                dp[i][k] = dp[i - 1][k]

    return dp[n][m]
