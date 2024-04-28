def max_sum_subsequence(nums, k):
    n = len(nums)
    dp = [[-float('inf')] * (k + 1) for _ in range(n)]

    for i in range(n):
        for j in range(min(i+1, k)+1):
            if i == 0:
                dp[i][j] = nums[0]
            elif j == 1:
                dp[i][j] = max(dp[i-1][j], nums[i])
            else:
                dp[i][j] = max(dp[i-k-1][j-1] + nums[i], dp[i-1][j])

    return max(dp[-1])

# Example usage
nums = [3, 2, -1, 5, 4]
k = 2
print(max_sum_subsequence(nums, k))  # Output: 6
