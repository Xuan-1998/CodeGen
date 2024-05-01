def longestSubarray(nums):
    n = len(nums)
    dp = [0] * n
    max_length = 0

    for i in range(n):
        if nums[i] == 1:
            dp[i] = 1 + (i > 0 and nums[i-1] == 1) or dp[i-1]
        else:
            dp[i] = 1

        max_length = max(max_length, dp[i])

    return max_length
