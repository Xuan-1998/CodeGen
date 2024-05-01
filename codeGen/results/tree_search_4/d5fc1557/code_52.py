def longestSubarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)
    memo = {}
    
    for i in range(n - 1, -1, -1):
        if nums[i] == 1:
            j = i
            while j < n and nums[j] == 1:
                j += 1
            dp[i] = max(dp[i], j - i)
            memo[i] = j - i
        else:
            dp[i] = 0
    
    return max((dp[i] for i in range(n) if i > 0), default=0)

# Example usage:
nums = [1, 1, 0, 1]
print(longestSubarray(nums))  # Output: 2
