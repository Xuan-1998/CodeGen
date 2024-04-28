from functools import lru_cache

def solve(n, m):
    @lru_cache(None)
    def dfs(i, s):
        if s % m == 0:
            return True
        if i < 0 or s >= m:
            return False
        return dfs(i-1, s+arr[i]) or dfs(i-1, s)

    arr = list(map(int, input().split()))
    res = any(dfs(n-1, 0) for _ in range(2**n))
    print(1 if res else 0)
