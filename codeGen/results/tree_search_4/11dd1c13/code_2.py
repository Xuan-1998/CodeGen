from collections import defaultdict

def min_falling_path_sum(grid):
    n = len(grid)
    m = len(grid[0])
    dp = [[float('inf')] * (m) for _ in range(n)]
    dp[0] = [grid[0][j] for j in range(m)]

    memo = defaultdict(int)

    def dfs(i, j):
        if i == 0:
            return grid[i][j]
        if (i, j) in memo:
            return memo[(i, j)]
        min_sum = float('inf')
        for k in range(n):
            if k != i and k != i - 1:  # non-zero shifts
                min_sum = min(min_sum, dp[k][j] + grid[i][j])
        memo[(i, j)] = min_sum
        return min_sum

    return min(dfs(i, j) for i in range(n-1) for j in range(m))

# Example usage:
grid = [[1, 2], [3, 4]]
print(min_falling_path_sum(grid))  # Output: 5
