def longestSubarray(nums):
    n = len(nums)
    dp = [0] * n
    for i in range(n - 1, -1, -1):
        if nums[i] == 1:
            dp[i] = max(dp[i], dp[i+1]) + 1
        else:
            dp[i] = dp[i+1]
    return max((i for i in range(n) if dp[i] > 0), default=0)
