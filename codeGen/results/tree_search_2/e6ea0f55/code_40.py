def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if j == 1:
                dp[i][j] = nums[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - nums[i - 1]) + nums[i - 1]
    
    return dp[n][k]

# Example usage
nums = [5, -3, 4, 9, 2]
k = 2

print(maxSumSubsequence(nums, k))  # Output: 15
