def maxSumOfSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(k + 1):
        dp[0][i] = float('-inf')

    for i in range(1, n):
        for j in range(min(i + 1, k + 1)):
            if j == 0:
                dp[i][j] = nums[i]
            else:
                dp[i][j] = max(dp[max(0, i - k)][j - 1] + nums[i], dp[i - 1][j])

    return max(dp[-1])
