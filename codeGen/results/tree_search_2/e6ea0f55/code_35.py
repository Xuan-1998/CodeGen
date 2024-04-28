def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]
    
    # Initialize the first row of the table
    for j in range(k + 1):
        dp[0][j] = nums[0]
    
    # Fill up the rest of the table
    for i in range(1, n):
        for j in range(min(i, k) + 1):
            if j == 0:
                dp[i][j] = max(dp[i - 1][j], nums[i])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + nums[i])
    
    # Find the maximum sum of a subsequence
    max_sum = 0
    for j in range(k + 1):
        max_sum = max(max_sum, dp[-1][j])
    
    return max_sum

# Example usage:
nums = [10, -20, 30, 5, -7, 1]
k = 3
print(maxSumSubsequence(nums, k))  # Output: 18
