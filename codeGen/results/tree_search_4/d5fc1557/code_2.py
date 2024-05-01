def longestSubarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)

    if nums[0] == 1:
        dp[0] = 1
    else:
        dp[0] = 0

    for i in range(1, n + 1):
        if nums[i-1] == 1 and dp[i-1] != 0:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = 1

    return max(dp) - 1
