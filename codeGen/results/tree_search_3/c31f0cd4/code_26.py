def distinct_sum_sets(nums):
    n = len(nums)
    sums = set()
    dp = [[0] * (sum(nums) + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(sum(nums) + 1):
            if nums[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i - 1]] + nums[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    for i in range(1, n + 1):
        for j in range(sum(nums) + 1):
            if dp[i][j] > 0:
                sums.add(j)

    return ' '.join(map(str, sorted(list(sums))))
