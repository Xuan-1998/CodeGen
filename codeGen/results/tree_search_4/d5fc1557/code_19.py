def longest_ones_subarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)

    for i in range(n):
        if nums[i] == 1:
            dp[i + 1] = max(dp[i], dp[i] + 1)
        else:
            dp[i + 1] = dp[i]

    return max(0, dp[-1])
