def maxSumSubsequence(nums, k):
    nums.sort()
    dp = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        dp[i+1] = max(dp[i], nums[i] + dp[max(0, i-k)])
    return dp[-1]

nums = [int(i) for i in input().split()]
k = int(input())
print(maxSumSubsequence(nums, k))
