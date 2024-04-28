def maxSumSubsequence(nums, k):
    n = len(nums)
    memo = {}
    
    def dp(i, sum):
        if (i, sum) in memo:
            return memo[(i, sum)]
        
        if i < 0 or i >= n:
            return 0
        
        res = sum
        for j in range(max(0, i-k), min(n, i+k+1)):
            res = max(res, dp(j-1, sum-nums[j]) + nums[i])
        
        memo[(i, sum)] = res
        return res
    
    return max(dp(i, 0) for i in range(k, n))
