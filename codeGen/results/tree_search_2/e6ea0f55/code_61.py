def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if nums[i - 1] - nums[i - 2] <= j:
                dp[i][j] = max(dp[i - 1][j], nums[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    
    return sum(nums) + sum(range(1, k + 1)) - dp[n][k]

import sys
input = sys.stdin.read().split()
nums = list(map(int, input[0].split(',')))
k = int(input[1])
print(maxSumSubsequence(nums, k))
