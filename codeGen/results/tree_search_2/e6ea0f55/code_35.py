from functools import lru_cache

@lru_cache(None)
def max_sum(i: int, j: int) -> int:
    if i < 0 or j <= 0:
        return 0
    if abs(i - (j-1)) > k:
        return 0
    return nums[i] + max(max_sum(i-k, j-1), 0)

k = int(input())
nums = [int(x) for x in input().split()]
max_val = max(nums)
dp = [[0]*len(nums) for _ in range(max_val+1)]

for i in range(len(nums)):
    for j in range(1, min(i+k+1, len(nums)+1)):
        dp[j][i] = max(dp[j-1][i-k] if i >= k else 0, nums[i]) + dp[j-1][i]

print(max(map(max, dp)))
