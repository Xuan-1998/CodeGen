def longestSubarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)

    def dfs(i):
        if i >= n:
            return 0
        if dp[i]:
            return dp[i]
        
        result = 1 if nums[i] == '1' else 0
        
        for j in range(i, -1, -1):
            if nums[j] != '1':
                break
            result = max(result, dfs(j) + 1)
        
        dp[i] = result
        return result

    return max(dfs(i) for i in range(n))

# Input your array and test the function
nums = input().split()
print(longestSubarray(nums))
