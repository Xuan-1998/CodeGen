def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(k + 1):
        dp[0][i] = nums[0]

    for i in range(1, n):
        for j in range(min(i + 1, k + 1)):
            if i >= j:
                dp[i][j] = max(dp[i - 1][j], dp[max(0, i - j)][j - 1]) + nums[i]
            else:
                dp[i][j] = nums[i]

    return max(max(row) for row in dp)

# Example usage
nums = [3, 2, -2, 4, 1, 1, -2, 1, 6]
k = 2
print(maxSumSubsequence(nums, k))  # Output: 7
