from functools import lru_cache

def canReach(arr):
    @lru_cache(None)
    def helper(i, reachable):
        if i == len(arr) - 1:
            return True
        if not reachable or i < 0:
            return False
        j = min(i + arr[i], len(arr) - 1)
        for k in range(i + 1, j + 1):
            if helper(k, reachable and k <= j):
                return True
        return False

    return helper(0, True)

arr = list(map(int, input().split()))
print(canReach(arr))
