from typing import List

def maxSumSubsequence(nums: List[int], k: int) -> int:
    n = len(nums)
    dp = [0] * (n + 1)
    
    for i in range(n):
        dp[i + 1] = max(dp[i], nums[i])
        
    for i in range(k, n):
        dp[i + 1] = max(dp[i], dp[i - k] + nums[i])
        
    return dp[-1]
