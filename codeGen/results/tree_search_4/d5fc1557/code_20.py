def longest_subarray(nums):
    n = len(nums)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if nums[i - 1] == 1:
            dp[i] = max(dp[i - 1] + 1, n - i + 1)
        else:
            dp[i] = max(dp[i - 1], n - i)

    return max(dp) - 1
