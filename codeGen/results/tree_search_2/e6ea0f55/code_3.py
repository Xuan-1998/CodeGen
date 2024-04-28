def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(n - 1, -1, -1):
        for j in range(min(i, k), -1, -1):
            if i == n - 1:
                dp[i][j] = nums[i]
            else:
                dp[i][j] = max(dp[i + 1][j], nums[i] + dp[i + 1].get(j - (i + 1 - j), 0))

    return dp[0].index(max(dp[0]))

nums = list(map(int, input().split()))
k = int(input())
print(maxSumSubsequence(nums, k))
