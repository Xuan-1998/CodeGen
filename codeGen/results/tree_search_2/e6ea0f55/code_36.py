import sys
from collections import defaultdict

def maxSumSubsequence(nums, k):
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]

    for i in range(n):
        for j in range(min(i + 1, k) + 1):
            if i == 0:
                dp[i][j] = nums[i]
            elif j == 0:
                dp[i][j] = max(dp[i - 1][j], nums[i])
            else:
                dp[i][j] = max(dp[i - 1][j], nums[i] + dp[i - 1][j - 1])

    return dp[-1][-1]

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    k = int(input())
    print(maxSumSubsequence(nums, k))
