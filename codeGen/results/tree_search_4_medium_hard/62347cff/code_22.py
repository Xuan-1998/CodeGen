def min_path_sum(grid):
    m, n = len(grid) - 1, len(grid[0]) - 1

    dp = [[0] * (n + 1) for _ in range(m + 1)]
    cache = {}

    def min_sum(i, j):
        if i < 0 or j < 0:
            return float('inf')
        if i == m and j == n:
            return grid[i][j]
        key = (i, j)
        if key in cache:
            return cache[key]

        result = min(grid[i][j] + dp[i-1][j], grid[i][j] + dp[i][j-1])
        cache[key] = result
        return result

    for i in range(m + 1):
        dp[i][0] = 0
    for j in range(n + 1):
        dp[0][j] = 0

    return min_sum(0, 0)
