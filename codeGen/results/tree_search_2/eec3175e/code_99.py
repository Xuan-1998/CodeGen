def subsetSumDivisible(nums, m):
    n = len(nums)
    dp = {0: True}
    
    for x in nums:
        temp = dict()
        for j in sorted(dp.keys()):
            if (j + x) % m not in temp:
                temp[(j + x) % m] = dp[j]
        dp.update(temp)

    return 1 if m in dp else 0
