def maxSum(nums, k):
    n = len(nums)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    # Initialize the base case
    for j in range(1, n + 1):
        dp[0][j] = max(dp[0][j - 1], nums[j - 1])

    # Fill up the table using the given constraint
    for i in range(1, n + 1):
        for j in range(1, min(i + k + 1, n + 1)):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + nums[i - 1])

    # Return the maximum sum of a subsequence
    return max(max(row) for row in dp)

# Example usage:
nums = [1, 2, 3, 4]
k = 2
print(maxSum(nums, k))  # Output: 10

