from functools import lru_cache

@lru_cache(None)
def dp(i, j):
    if i == 0:
        return grid[i][j]
    min_sum = float('inf')
    for k in range(len(grid[0])):
        min_sum = min(min_sum, dp(i-1, k) + grid[i][j])
    return min_sum

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
print(min(dp(i, j) for i in range(n) for j in range(len(grid[0]))))
