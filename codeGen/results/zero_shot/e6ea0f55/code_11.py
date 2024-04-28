from typing import List

def max_sum_subsequence(nums: List[int], k: int) -> int:
    n = len(nums)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = max(dp[i-1], nums[i-1])
        for j in range(1, min(i, k)+1):
            if i-j > 0:
                dp[i] = max(dp[i], dp[i-j] + nums[i-1])
    return dp[-1]
