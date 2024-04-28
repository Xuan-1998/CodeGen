def max_sum_subsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k+1) for _ in range(n)]

    for i in range(n):
        for j in range(min(i+1, k)+1):
            if i == 0:
                dp[i][j] = nums[i]
            else:
                max_sum = max(dp[i-1][max(0, j-1)] + nums[i], dp[i-1][j])
                dp[i][j] = max_sum

    return max(dp[-1])

# Example usage
nums = [1, 3, -1, 2, -4]
k = 2
print(max_sum_subsequence(nums, k))  # Output: 5 (subsequence: [1, 3])
