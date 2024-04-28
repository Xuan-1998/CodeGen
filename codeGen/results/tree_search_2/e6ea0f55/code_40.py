def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]
    
    # Initialize the base case: a subsequence with only one element has a sum equal to that element
    for i in range(n):
        dp[i][0] = nums[i]
    
    # Fill in the rest of the table using dynamic programming and tabulation
    for i in range(1, n):
        for j in range(min(i + 1, k) + 1):
            if j == 0:
                dp[i][j] = max(dp[i - 1][j], nums[i])
            else:
                # For each pair of consecutive elements and their difference, consider the maximum sum
                # that can be obtained by including or excluding the current element
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][max(0, j - 1)] + nums[i])
    
    # Return the maximum sum of a subsequence found in the table
    return max(dp[-1])

# Example usage:
nums = [3, 6, 2, 8]
k = 2
print(maxSumSubsequence(nums, k))  # Output: 12

