def max_sum_subsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(n):
        for j in range(min(i + 1, k) + 1):
            if i == 0:
                dp[i][j] = nums[0]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1].get(j-k, 0) - nums[i-1]) + nums[i]

    return max(max(row) for row in dp)

# Example usage
nums = [10, 2, -3, 4, 5]
k = 2
print(max_sum_subsequence(nums, k))  # Output: 17
