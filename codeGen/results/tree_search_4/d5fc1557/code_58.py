def longestSubarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)
    max_length = 0

    for i in range(1, n + 1):
        if nums[i - 1] == 1 and (i < 2 or nums[i - 2] == 1):
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 1

        max_length = max(max_length, dp[i])

    return max_length if max_length > 0 else 0
