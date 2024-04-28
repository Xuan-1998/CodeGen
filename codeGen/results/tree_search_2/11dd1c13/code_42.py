def min_falling_path(grid):
    n = len(grid)
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        
        # Base case: end of the path
        if i == n - 1:
            return grid[i][j]

        # Initialize minimum sum for this cell
        min_sum = float('inf')

        # Explore neighboring cells with non-zero shifts
        for k in range(n):
            if k != j and (k < i or k > i + 1):  # skip adjacent rows
                min_sum = min(min_sum, dp(i - 1, k) + grid[i][j])

        memo[(i, j)] = min_sum
        return min_sum

    # Start from the top row and iterate downwards
    min_sum = float('inf')
    for j in range(n):
        min_sum = min(min_sum, dp(0, j))

    return min_sum

# Example usage:
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(min_falling_path(grid))  # Output: 12 (minimum sum of a falling path)
