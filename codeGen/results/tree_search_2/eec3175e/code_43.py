from functools import lru_cache

@lru_cache(None)
def dp(i, s):
    if s == 0:
        return True
    if i >= len(nums) or s < 0 or (i > 0 and nums[i-1] > s):
        return False
    return dp(i+1, s-nums[i-1]) or dp(i+1, s)

n, m = map(int, input().split())
nums = list(map(int, input().split()))

if dp(0, m):
    print(1)
else:
    print(0)
