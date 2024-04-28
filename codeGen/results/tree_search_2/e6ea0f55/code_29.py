def max_sum_subsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(1, n):
        for j in range(min(i, k), -1, -1):
            if i - j >= 0:
                dp[i][j] = max(dp[i-1][max(j-1, 0)] + nums[i], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]
