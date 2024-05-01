def longest_ones(nums):
    n = len(nums)
    dp = {0: nums[0] if nums[0] == 1 else 0}

    for i in range(1, n):
        if nums[i] == 1:
            dp[i] = max(dp.get(i-1, 0) + 1, 1)
        else:
            dp[i] = 0

    return max(dp.values()) - 1
