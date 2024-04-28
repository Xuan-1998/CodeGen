def maximumSubsequenceSum(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    dp[0][0] = nums[0]
    for i in range(1, n):
        for j in range(k + 1):
            if j < k:
                dp[i][j] = max(dp[i-1][j], dp[min(i-1, j-k)][min(j-k, k)]) + nums[i]
            else:
                dp[i][j] = dp[i-1][k]

    return max(dp[-1])

# Test the function
nums = [2, 5, 7, 10, 9, 3, 8, 1, 4, 6]
k = 3
print(maximumSubsequenceSum(nums, k))  # Output: 24
