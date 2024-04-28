def longestSubarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)  # Initialize DP array with zeros
    max_len = 0

    for i in range(n):
        if nums[i] == 1:  # If the current element is 1, update max_len
            dp[i + 1] = dp[i] + 1
            max_len = max(max_len, dp[i + 1])
        else:
            dp[i + 1] = 0

    return max_len - 1 if max_len > 0 else 0

# Example usage:
nums = [1, 1, 0, 1]
print(longestSubarray(nums))  # Output: 2
