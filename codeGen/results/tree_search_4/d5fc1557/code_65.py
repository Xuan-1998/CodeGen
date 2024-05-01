def longest_subarray(nums):
    n = len(nums)
    dp = [0] * n

    for i in range(n - 1):
        if nums[i] == 1:
            dp[i + 1] = max(dp[i], 1) if i == 0 else max(dp[i], dp[i - 1]) + 1
        else:
            dp[i + 1] = dp[i]

    return max(dp)

# Example usage
nums = [1, 1, 0, 1, 1, 1]
print(longest_subarray(nums))  # Output: 4
