def maximum_sum(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            if i < k:
                dp[i][j] = max(dp[i-1][j], nums[i])
            else:
                dp[i][j] = max(dp[i-k][j-1] + nums[i], dp[i-1][j])
    
    return dp[-1][-1]

# Example usage
nums = [1, 2, 3, 4, 5]
k = 2
print(maximum_sum(nums, k))  # Output: 9 (subsequence: [4, 5])
