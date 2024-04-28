def maxSubsequence(nums, k):
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    dp = [[0] * (k + 1) for _ in range(k + 1)]
    for gap in range(1, k + 1):
        for left in range(gap):
            if left == 0:
                dp[gap][left] = prefix_sum[gap]
            else:
                dp[gap][left] = max(dp[gap - 1][left - 1], prefix_sum[left + gap] - prefix_sum[left])

    return dp[k][k]
