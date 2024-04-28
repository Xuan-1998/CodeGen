def longestSubarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)
    max_length = 0

    for i in range(n):
        if nums[i] == 1:
            dp[i + 1] = dp[i] + 1
            max_length = max(max_length, dp[i + 1])
        else:
            dp[i + 1] = 0

    return max_length - (dp[n] > 0)
