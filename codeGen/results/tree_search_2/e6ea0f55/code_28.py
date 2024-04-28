def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = {0: nums[0]}
    
    for i in range(1, n):
        for j in range(min(i, k), -1, -1):
            if i - j >= 0 and j <= k:
                dp[i] = max(dp.get(i-1, 0) + nums[i], dp.get(i-j, 0) + nums[i])
    return max(dp.values())

nums = list(map(int, input().split()))
k = int(input())
print(maxSumSubsequence(nums, k))
