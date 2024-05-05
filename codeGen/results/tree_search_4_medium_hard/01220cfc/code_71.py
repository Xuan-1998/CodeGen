from functools import lru_cache

def can_jump(arr):
    @lru_cache(None)
    def dfs(i, reachable):
        if i == len(arr) - 1:
            return True
        if not reachable:
            return False
        for j in range(min(i + arr[i], len(arr) - 1), -1, -1):
            if dfs(j, False):
                return True
        return False

    return dfs(0, True)
