def maxSumOfSubsequence(nums, k):
    n = len(nums)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if i <= k:
            dp[i] = sum(nums[:i+1])
        else:
            dp[i] = max(dp[i-1], dp[i-k-1] + nums[i])

    return dp[-1]

# Example usage
nums = [1, -2, 3, 10, -4, 7]
k = 2

print(maxSumOfSubsequence(nums, k))  # Output: 14
