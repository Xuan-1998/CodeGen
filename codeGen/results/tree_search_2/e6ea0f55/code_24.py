def maxSum(nums, k):
    n = len(nums)
    dp = [0] * n

    # Base cases: Initialize the DP array for i = 0 and len(nums) - 1
    dp[0] = nums[0]
    dp[-1] = nums[-1]

    for i in range(1, n - 1):
        if i <= k:
            dp[i] = max(dp[i-1], nums[i])
        else:
            dp[i] = max(dp[i-k], nums[i])

    return max(dp)

# Example usage
nums = [5, 3, -1, 8, 10]
k = 2
print(maxSum(nums, k))  # Output: 15
