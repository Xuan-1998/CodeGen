from collections import deque

def minInitialPoints(grid):
    m, n = len(grid), len(grid[0])
    memo = {}

    def dfs(i, j, points):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == m - 1 and j == n - 1:
            return points
        min_points = float('inf')
        if i < m - 1:
            min_points = min(min_points, dfs(i + 1, j, points + grid[i][j]))
        if j < n - 1:
            min_points = min(min_points, dfs(i, j + 1, points + grid[i][j]))
        memo[(i, j)] = min_points
        return min_points

    return dfs(0, 0, 0)

if __name__ == "__main__":
    N, M = map(int, input().split())
    grid = [[int(x) for x in input().split()] for _ in range(M)]
    print(minInitialPoints(grid))
