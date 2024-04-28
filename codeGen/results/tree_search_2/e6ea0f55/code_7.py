def maxSum(nums, k):
    n = len(nums)
    m = max(nums) + k  # upper bound for the maximum sum
    dp = [[0]*(m+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(max(0, m-nums[i]), min(m+1, m+1)):
            dp[i][j] = max(dp[i-1][max(0, j-nums[i])]+nums[i], dp[i-1][j])

    return dp[n][m]
