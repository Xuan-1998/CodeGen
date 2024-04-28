def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        if i <= k:
            dp[i] = nums[i - 1]
        else:
            dp[i] = max(dp[i - 1], nums[i - 1] + dp[max(0, i - k)])
    
    return dp[n]

# Example usage
nums = [10, 12, 7, 9, 2, 11, 5, 3]
k = 2

print(maxSumSubsequence(nums, k))
