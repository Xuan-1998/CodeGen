def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(1, n):
        for j in range(min(i, k) + 1):
            if j == 0:
                dp[i][j] = max(dp[i-1][j], nums[i])
            else:
                dp[i][j] = max(dp[i-1][j-1] + nums[i], nums[i])

    return max(sum(subsequence) for subsequence in zip(*dp))

import sys
input = sys.stdin.readline

nums = list(map(int, input().split()))
k = int(input())

print(maxSumSubsequence(nums, k))
