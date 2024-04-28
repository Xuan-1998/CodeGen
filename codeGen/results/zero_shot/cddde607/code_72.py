import sys
from functools import lru_cache

K, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

@lru_cache(None)
def dfs(i, j, k):
    if i == N - 1 and j == N - 1:
        return 1
    if i >= N or j >= N or k < 0:
        return 0
    return dfs(i + 1, j, k - arr[i][j]) + dfs(i, j + 1, k - arr[i][j])

print(dfs(0, 0, K))
