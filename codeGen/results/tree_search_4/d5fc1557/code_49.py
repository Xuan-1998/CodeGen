def longest_subarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if nums[i - 1] == 0:
            dp[i] = 0
        elif i > 0 and nums[i - 1] == nums[i - 2]:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = 1

    return max(dp) if any(dp) else 0
