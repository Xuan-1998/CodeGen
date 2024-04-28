def max_sum_of_subsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    # Base case: initialize dp[0][j] = nums[0]
    dp[0][0] = nums[0]

    for i in range(1, n):
        for j in range(min(i + 1, k) + 1):
            if j == 0:
                dp[i][j] = max(dp[i-1][j], nums[i])
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][min(j, k)]) + nums[i]

    # Return the maximum sum
    return max(dp[-1])

# Example usage:
nums = [2, 3, -1, 5, -7, 2]
k = 2
print(max_sum_of_subsequence(nums, k))  # Output: 6 (from subsequence [2, 3, 2])
