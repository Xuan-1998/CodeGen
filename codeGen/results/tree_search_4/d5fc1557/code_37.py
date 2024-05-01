def longestSubarray(nums):
    dp = {i: 0 for i in range(len(nums))}
    max_len = 0

    for i in range(1, len(nums)):
        if nums[i] == 1 and (dp.get(i-1) == None or nums[i-1] != 1):
            dp[i] = dp.get(i-1, 0) + 1
            max_len = max(max_len, dp[i])

    return max_len

# Example usage:
nums = [1,0,1,1,0,1]
print(longestSubarray(nums))  # Output: 3
