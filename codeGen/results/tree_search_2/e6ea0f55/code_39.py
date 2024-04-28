def max_sum_subsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(k + 1):
        dp[0][i] = nums[0]

    for i in range(1, n):
        for diff in range(min(i + 1, k) + 1):
            if diff == 0:
                dp[i][diff] = max(dp[i - 1][diff], nums[i])
            else:
                dp[i][diff] = max(dp[i - 1][diff], dp[i - 1][diff - 1] - nums[i - 1] + nums[i])

    return max(dp[-1])

# Example usage
nums = [10, 3, 2, 5, 7]
k = 2

print(max_sum_subsequence(nums, k))
