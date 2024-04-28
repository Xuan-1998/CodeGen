def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(n):
        for j in range(min(i + 1, k) + 1):
            if i == 0:
                dp[i][j] = nums[0]
            else:
                dp[i][j] = max(dp[i - 1][j], nums[i]) if j > 0 or i == 0 else nums[i]

    return max(max(row) for row in dp)

import sys
input = lambda: [int(i) for i in input().split()]
n, k = input()
nums = list(map(int, input()))
print(maxSumSubsequence(nums, k))
