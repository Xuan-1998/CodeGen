def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]
    
    for i in range(n):
        for j in range(min(i, k) + 1):
            if i == 0:
                dp[i][j] = nums[i]
            else:
                dp[i][j] = max(dp[i - 1][j], nums[i] + dp[max(0, i - j - 1)][j - 1] if j > 0 else nums[i])
    
    return max(max(row) for row in dp)

import sys
input = lambda: [int(i) for i in input().split()]
nums, k = input()
print(maxSumSubsequence(nums, k))
