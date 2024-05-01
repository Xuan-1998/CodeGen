def longest_subarray(nums):
    n = len(nums)
    dp = [0] * n

    for i in range(1, n):
        if nums[i] == 1:
            if i > 0 and dp[i - 1] > 0:
                dp[i] = max(dp[i], dp[i - 1] + 1)
            else:
                dp[i] = 1
        else:
            dp[i] = 0

    return max(dp) if any(dp) else 0
