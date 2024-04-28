def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[-10**4] * (k + 1) for _ in range(n)]

    for i in range(1, n):
        for j in range(min(i, k) + 1):
            if i == 1:
                dp[i][j] = max(dp[0][k], nums[i])
            else:
                dp[i][j] = max((dp[i-1][min(k, j)] or -10**4) + nums[i], j + 1)

    return max(dp[-1])
