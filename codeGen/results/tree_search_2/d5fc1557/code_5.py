def longestSubarray(nums):
    memo = {}

    def dfs(i):
        if i == len(nums):
            return 0
        if i in memo:
            return memo[i]
        
        res = 0
        count = 0

        while i < len(nums) and nums[i] == 1:
            count += 1
            i += 1
        
        if count > res:
            res = count

        if i < len(nums):
            res = max(res, dfs(i + 1))

        memo[i] = res
        return res
    
    return dfs(0)
