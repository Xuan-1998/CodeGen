def max_sum_subsequence(nums, k):
    n = len(nums)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(min(i, k), -1, -1):
            if i - j >= 0:
                dp[i] = max(dp[i], dp[i - j] + nums[i])

    return max(dp)
