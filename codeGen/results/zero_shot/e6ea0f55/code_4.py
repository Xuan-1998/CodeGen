def maxSubsequenceSum(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]
    
    for i in range(1, n):
        for j in range(min(i, k), -1, -1):
            dp[i][j] = max(dp[i-1][j], nums[i] + dp[i-j-1][j-1] if j > 0 else nums[i])
    
    return dp[-1][-1]
