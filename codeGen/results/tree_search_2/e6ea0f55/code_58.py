def max_subsequence_sum(nums, k):
    n = len(nums)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(min(i, k), -1, -1):
            if j == 0:
                dp[i][j] = nums[i - 1]
            else:
                dp[i][j] = max(dp[j - 1][max(0, j - k)] + nums[i - 1], dp[j][j])
    return dp[-1][-1]

# Example usage
nums = [3, 2, -2, -5, 6, 4, -3]
k = 2
print(max_subsequence_sum(nums, k))  # Output: 8
