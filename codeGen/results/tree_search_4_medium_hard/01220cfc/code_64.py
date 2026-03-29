from functools import lru_cache

def canJump(nums):
    @lru_cache(None)
    def dfs(i):
        if i >= len(nums) - 1:
            return True
        
        max_reachable = nums[i]
        for j in range(i + 1, min(i + max_reachable + 1, len(nums))):
            if dfs(j):
                return True
        return False

    return dfs(0)
