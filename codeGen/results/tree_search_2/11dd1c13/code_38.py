import sys
from functools import lru_cache

def min_falling_path_sum(grid):
    n = len(grid)
    @lru_cache(None)
    def dp(i, j):
        if i == 0:
            return grid[i][j]
        res = float('inf')
        for k in range(j+1, len(grid[0])):
            res = min(res, dp(i-1, k) + grid[i][j])
        return res

    return min([dp(n-1, j) for j in range(len(grid[0]))])

if __name__ == "__main__":
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(min_falling_path_sum(grid))
