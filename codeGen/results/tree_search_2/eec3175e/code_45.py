from functools import lru_cache

@lru_cache(None)
def dfs(i, total):
    if total % m == 0:
        return True
    if i >= len(arr) or total > m:
        return False
    return dfs(i + 1, total) or dfs(i + 1, total + arr[i])

n, m = map(int, input().split())
arr = list(map(int, input().split()))
print(1 if dfs(0, 0) else 0)
