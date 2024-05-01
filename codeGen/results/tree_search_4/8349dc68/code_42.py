def maxSumAfterPartitioning(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            max_val = nums[i - 1]
            for l in range(j, 0, -1):
                max_val = max(max_val, dp[i - l][j - 1] + nums[i - l])
            dp[i][j] = max(dp[i - 1][j], dp[i - j][j] + max_val)

    return dp[n][k]

# Example usage
nums = [1, 14, 5, 10]
k = 3

print(maxSumAfterPartitioning(nums, k))
