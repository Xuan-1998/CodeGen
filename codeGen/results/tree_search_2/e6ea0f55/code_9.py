def maxSumOfSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(1, n):
        for j in range(min(i, k) + 1):
            if j == 0:
                dp[i][j] = nums[i]
            else:
                dp[i][j] = max(dp[i-1][min(j-1, k)], dp[i-1][j-1]) + nums[i]

    return max(max(row[k:]) for row in dp)
