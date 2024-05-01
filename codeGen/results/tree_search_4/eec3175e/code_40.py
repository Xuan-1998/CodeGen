def can_sum_divisible_by_m(nums, m):
    dp = [False] * (m + 1)
    dp[0] = True

    for num in nums:
        for i in range(m, -1, -1):
            if i >= num and not dp[i - num]:
                dp[i] = True
                break

    return dp[m]
