from functools import lru_cache

def can_sum_divisible_by_m(n, m, nums):
    @lru_cache(maxsize=None)
    def dp(i, s):
        if s % m == 0:  # Found a subset with sum divisible by m
            return True
        if i < 0 or s > sum(nums[:i+1]):  # Out of bounds or exceeded the maximum sum
            return False
        return any(dp(j, s - num) for j in range(i))

    memo = {}
    for i in range(n):
        for s in range(sum(nums[:i+1]) + 1):  # Iterate over all possible sums up to the current sum
            memo[(i, s)] = dp(i, s)

    return any(memo[i, j] for i in range(n) for j in range(sum(nums[:i+1]) + 1))
