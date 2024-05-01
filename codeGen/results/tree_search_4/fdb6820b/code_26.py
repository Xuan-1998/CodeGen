def count_ways(m, N, nums):
    dp = [0] * (N + 1)
    dp[0] = 1

    for i in range(1, N + 1):
        for num in nums:
            if i >= num:
                dp[i] += dp[i - num]

    return dp[N]
