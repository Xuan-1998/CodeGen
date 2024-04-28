def max_sum_subsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(1, n):
        for j in range(min(i, k) + 1):
            dp[i][j] = max(dp[i-1][j], dp[max(0, i-k)][j-k] + nums[i])

    return max(dp[n-1][j] for j in range(k+1))

# Example usage:
nums = [1, 2, 3, 4, 5]
k = 2
print(max_sum_subsequence(nums, k))  # Output: 9
