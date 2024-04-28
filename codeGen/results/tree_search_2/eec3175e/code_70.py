from functools import lru_cache

def solve(n, m, arr):
    @lru_cache(None)
    def dp(i, s):
        if s % m == 0:
            return 1
        if i >= n or s < 0:
            return 0
        return max(dp(i + 1, s), dp(i + 1, s - arr[i]))

    return dp(0, 0)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(solve(n, m, arr))
