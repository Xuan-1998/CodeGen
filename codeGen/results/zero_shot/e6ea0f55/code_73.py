def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]
    
    for i in range(k + 1):
        dp[0][i] = nums[0]
    
    for i in range(1, n):
        for j in range(min(i, k), -1, -1):
            dp[i][j] = max(dp[i-1][j], dp[i-1][min(j, k)] + nums[i])
    
    return max(sum(sub) for sub in zip(*dp))
