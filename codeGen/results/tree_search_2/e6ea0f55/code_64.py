codeblock
def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(k+1):
        dp[0][i] = nums[0]

    for i in range(1, n):
        for j in range(min(i+1, k)+1):
            if j == 0:
                dp[i][j] = nums[i]
            else:
                max_sum = 0
                for p in range(max(0, i-j), i):
                    max_sum = max(max_sum, dp[p][j-1])
                dp[i][j] = max_sum + nums[i]

    return max(dp[-1])
