def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if i == 1:
                dp[i][j] = nums[0]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + nums[i - 1])
            if j > 0 and i >= k:
                dp[i][j] = max(dp[i][j], dp[i - k][j] + nums[i - 1])

    return dp[n][k]
