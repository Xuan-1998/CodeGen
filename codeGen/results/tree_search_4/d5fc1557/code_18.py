def longestSubarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if nums[i - 1] == 1:
            dp[i] = max(dp[i-1], 1)
        else:
            dp[i] = dp[i-1]

    return dp[n]
