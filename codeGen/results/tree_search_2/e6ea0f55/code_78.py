def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    # Initialize the base case when i = 0
    dp[0][0] = nums[0]
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][0], nums[i])
    
    # Fill up the DP table using the given constraint
    for i in range(1, n):
        for j in range(min(i, k) + 1):
            if j == 0:
                dp[i][j] = max(dp[i-1][j], nums[i])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + nums[i])

    # Return the maximum sum of a non-empty subsequence
    return dp[-1][-1]

# Example usage:
nums = [4, 2, 3]
k = 1

print(maxSumSubsequence(nums, k))  # Output: 6
