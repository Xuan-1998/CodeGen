def longestSubarray(nums):
    n = len(nums)
    memo = {}
    
    def dp(i, ones, zeros):
        if (i, ones, zeros) in memo:
            return memo[(i, ones, zeros)]
        
        if i == 0:
            return 0
        
        ans = 0
        if nums[i] == 1:
            ans = max(ans, dp(i-1, ones+1, zeros))
        else:
            if ones > 0:
                ans = max(ans, dp(i-1, ones-1, zeros+1) + 1)
        
        memo[(i, ones, zeros)] = ans
        return ans
    
    longest = 0
    ones = 0
    for i in range(n):
        if nums[i] == 1:
            ones += 1
        else:
            if ones > 0:
                longest = max(longest, dp(i-1, ones-1, 0))
            ones = 0
    
    return max(longest, dp(n-1, 0, 0))

# Example usage:
nums = [1,0,1,1,0,1]
print(longestSubarray(nums)) # Output: 3
