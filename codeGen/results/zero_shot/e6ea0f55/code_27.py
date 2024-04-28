def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(min(i, k) + 1):
            dp[i][j] = max(dp[i-1][j], nums[i-1] + dp[i-j-1][min(j-1, k)])
    
    return dp[-1][-1]

n, k = map(int, input().split())
print(maxSumSubsequence(list(map(int, input().split())), k))
