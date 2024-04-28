def longestSubarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)

    for i in range(n + 1):
        if i == 0 or nums[i - 1] == 0:
            dp[i] = 0
        else:
            dp[i] = dp[i - 1] + 1

    max_len = 0
    for i in range(n):
        if nums[i] == 0:
            max_len = max(max_len, dp[i])
        elif i > 0 and nums[i - 1] == 1:
            max_len = max(max_len, dp[i])

    return max_len
