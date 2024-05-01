def maximum_ones(nums):
    n = len(nums)
    dp = [0] * (n + 1)
    memo = [-1] * (n + 1)

    for i in range(1, n + 1):
        if nums[i - 1] == 1:
            if memo[i - 1] >= 0:
                dp[i] = max(dp[i - 1], i - memo[i - 1])
            else:
                dp[i] = dp[i - 1]
        else:
            if memo[i - 1] >= 0:
                dp[i] = dp[i - 1]
            else:
                dp[i] = 1
        memo[i] = i

    return max(dp)
