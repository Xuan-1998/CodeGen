def maxSubsequenceSum(nums, k):
    memo = {}
    
    def dp(i):
        if (i, 0) in memo:
            return memo[(i, 0)]
        
        res = 0
        last_idx = i
        
        for j in range(max(0, i-k), i+1):
            s, l = dp(j)
            if l - j + k > i:
                s += nums[i]
                l = i
            elif l - j <= i - j and l - j + k >= 0:
                res = max(res, s + nums[i])
            else:
                res = max(res, l - j + k)
        
        memo[(i, 0)] = (res, last_idx)
        return res
    
    return dp(len(nums) - 1)[0]
