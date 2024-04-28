from functools import lru_cache

def find_subset(n, m):
    @lru_cache(None)
    def dfs(i, s):
        if s % m == 0:
            return True
        if i >= n or s > m:
            return False
        return dfs(i+1, s+a[i]) or dfs(i+1, s)

    a = list(map(int, input().split()))
    return int(dfs(0, 0))

n, m = map(int, input().split())
print(find_subset(n, m))
