def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = {}
    
    def dfs(i, prev_index):
        if (i, prev_index) in dp:
            return dp[(i, prev_index)]
        
        if i == 0:
            return nums[i]
        
        sum1 = nums[i] + dfs(prev_index-1, prev_index)
        sum2 = max(dfs(j-1, j-i) + nums[i] for j in range(prev_index+1, min(prev_index+k, n)))
        
        dp[(i, prev_index)] = max(sum1, sum2)
        return dp[(i, prev_index)]
    
    return dfs(n-1, 0)

