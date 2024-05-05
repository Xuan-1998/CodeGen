def min_points_to_reach_bottom_right(grid):
    N, M = len(grid), len(grid[0])
    dp = [[float('inf')] * M for _ in range(N)]

    def dfs(i, j, points):
        if i == N - 1 and j == M - 1:
            return points
        if i < N - 1 or j < M - 1:
            if grid[i][j] > 0:
                return min(dfs(i + 1, j, points), dfs(i, j + 1, points)) + grid[i][j]
            else:
                return float('inf')
        return float('inf')

    return dfs(0, 0, 0)

