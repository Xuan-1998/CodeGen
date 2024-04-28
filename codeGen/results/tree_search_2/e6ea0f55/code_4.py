from collections import defaultdict

def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]
    
    for i in range(k + 1):
        dp[0][i] = nums[0]
    
    for i in range(1, n):
        for j in range(min(i + 1, k + 1)):
            if i - j >= 0:
                dp[i][j] = max(dp[i-1][j], dp[i-j-1][j-1] + nums[i])
    
    return max(max(row) for row in dp)

nums = [int(x) for x in input().split()]
k = int(input())
print(maxSumSubsequence(nums, k))
