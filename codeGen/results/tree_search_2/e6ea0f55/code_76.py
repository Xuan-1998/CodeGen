from typing import List

def maxSumSubsequence(nums: List[int], k: int) -> int:
    n = len(nums)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(i, -1, -1):
            if i - j <= k:
                dp[i][j] = max(dp[i-1][j-1] + nums[j], nums[i])

    return max(sum(nums[i:j+1]) for i in range(n) for j in range(i+k, n))

# Example usage
nums = [1, 2, 3, 4, 5]
k = 1
print(maxSumSubsequence(nums, k))  # Output: 9 (subsequence [1, 3, 5])
