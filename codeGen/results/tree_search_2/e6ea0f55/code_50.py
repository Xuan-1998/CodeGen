def maxSum(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(1, n):
        for j in range(min(i, k) + 1):
            if abs(nums[i] - nums[i-1]) <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + nums[i])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]

