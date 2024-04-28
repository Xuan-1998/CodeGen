def max_sum_subsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(1, n):
        for j in range(min(i, k), -1, -1):
            if i <= j + k:
                dp[i][j] = max(dp[i-1][j-k], nums[i] + dp[i-1][min(j, k)])
            else:
                dp[i][j] = dp[i-1][j]
        for j in range(k, -1, -1):
            if i > j:
                dp[i][j] = max(dp[i-1][j], nums[i] + dp[i-1][min(j, k)])

    return max(dp[n-1])
