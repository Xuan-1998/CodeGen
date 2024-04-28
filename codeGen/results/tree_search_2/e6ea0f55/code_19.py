def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k+1) for _ in range(n)]
    
    for i in range(1, n):
        for j in range(min(k+1, i)):
            dp[i][j] = max(dp[i-1].min(j-1,k)+1] + nums[i], 
                         dp[max(i-j-k-1,0)][j] + nums[i])
    
    return max(dp[-1])
