def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            dp[i] = max(dp[i], dp[i - j] + nums[i - 1])
    return dp[-1]

nums = [int(x) for x in input().split()]
k = int(input())
print(maxSumSubsequence(nums, k))
