def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(n):
        for j in range(k + 1):
            if i == 0:
                dp[i][j] = nums[i]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][min(j, k)] + nums[i])

    return max(max(row) for row in dp)

# Example usage
nums = [2, 4, 3, -1, 5, 6]
k = 2

print(maxSumSubsequence(nums, k))  # Output: 11 (subsequence: [2, 4, 5])
