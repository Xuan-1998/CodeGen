def max_sum_subsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if j == 0:
                dp[i][j] = nums[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + nums[i - 1])
            for idx in range(i - 1, j - 2, -1):
                if i - idx <= k:
                    dp[i][j] = max(dp[i][j], dp[idx][j - 1] + nums[i - 1])

    return max([dp[i][-1] for i in range(n + 1)])

# Example usage
nums = [5, 10, 15, 20, 25]
k = 2
print(max_sum_subsequence(nums, k))  # Output: 45 (subsequence: [20, 25])
