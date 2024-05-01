def has_divisible_subset(n, m, nums):
    dp = {0: 1}
    for i in range(1, n+1):
        dp[i] = False
        for j in range(i):
            if (i - j) % m == 0 and dp.get(j, 0):
                dp[i] = True
                break

    return int(dp.get(n, 0))
