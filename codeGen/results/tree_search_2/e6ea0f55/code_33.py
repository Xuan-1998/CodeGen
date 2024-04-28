def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = {i: 0 for i in range(n)}
    
    for i in range(k+1, n):
        if i <= k:
            dp[i] = nums[i]
        else:
            dp[i] = max(dp[i-1], nums[i])
        
        for j in range(max(0, i-k), i):
            dp[i] = max(dp[i], dp[j] + nums[i])

    return max(dp.values())

k = int(input())
n = int(input())
nums = [int(x) for x in input().split()]

print(maxSumSubsequence(nums, k))
