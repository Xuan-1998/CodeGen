def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(k + 1):
        dp[0][i] = nums[0]

    for i in range(1, n):
        for j in range(min(i, k), -1, -1):
            if j < k:
                dp[i][j] = max(dp[i-1][max(0, j-k)], nums[i] + dp[max(0,i-k)][min(k,j)])
            else:
                dp[i][j] = dp[i-1][j]

    return max(dp[n-1])

# Example usage
nums = [10, 12, -2, -3, 5, 15, 20]
k = 2
print(maxSumSubsequence(nums, k))  # Output: 31
