import sys
from functools import lru_cache

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

@lru_cache(None)
def dfs(i, j, k):
    if i == N - 1 and j == N - 1:
        return 1 if arr[i][j] <= k else 0
    total = 0
    if i + 1 < N:
        total += dfs(i + 1, j, k - arr[i][j])
    if j + 1 < N:
        total += dfs(i, j + 1, k - arr[i][j])
    return total

print(dfs(0, 0, K))
