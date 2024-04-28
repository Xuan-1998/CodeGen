from typing import List

def maxSum(nums: List[int], k: int) -> int:
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            if i == j:
                dp[i][j] = nums[i - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + nums[i - 1])
    
    return dp[n][k]
