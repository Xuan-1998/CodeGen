def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(min(i, k), -1, -1):
            if i == 1:
                dp[i][j] = nums[0]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1].min() or dp[i-1][k]) + nums[i-1]

    return dp[n][k]

# Input from standard input
n, k = map(int, input().split())
nums = list(map(int, input().split()))

print(maxSumSubsequence(nums, k))
