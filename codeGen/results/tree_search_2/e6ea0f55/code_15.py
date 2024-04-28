def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    memo = {}
    
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if (i, j) not in memo:
                dp[i][j] = max(dp[max(i - 1, j - k)][max(j - k, 0)], nums[i - 1]) 
                memo[(i, j)] = dp[i][j]
    
    return dp[n][k]
