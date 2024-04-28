def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]
    
    for i in range(1, n):
        for j in range(min(i, k) + 1):
            if i - j > 0:
                dp[i][j] = max(dp[i-1][j-1] + nums[i], dp[i-1][j])
            else:
                dp[i][j] = nums[i]
                
    return dp[-1][-1]

n, k = map(int, input().split())
nums = list(map(int, input().split()))
print(maxSumSubsequence(nums, k))
