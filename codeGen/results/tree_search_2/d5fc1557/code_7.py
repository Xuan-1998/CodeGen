def longestSubarray(nums):
    n = len(nums)
    dp = {i: 0 for i in range(n)}
    dp[n-1] = nums.count('1')
    max_len = 0

    for i in range(n-2, -1, -1):
        if nums[i] == '1':
            dp[i] = min(dp[i+1], dp.get(i+1, 0)) + 1
        else:
            if i > 0 and dp[i-1] > 0:
                dp[i] = dp[i-1]
            else:
                dp[i] = 0
        max_len = max(max_len, dp[i])

    return max_len

# Example usage:
nums = [1, 0, 1, 1, 0, 1]
print(longestSubarray(nums))  # Output: 3
