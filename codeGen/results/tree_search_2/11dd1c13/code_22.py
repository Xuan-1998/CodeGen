from collections import defaultdict

def min_falling_path_sum(grid):
    n = len(grid)
    dp = defaultdict(int)

    for i in range(n):
        for j in range(n):
            if i == 0:
                dp[(i, j)] = grid[i][j]
            else:
                min_val = float('inf')
                for k in range(n):
                    if dp.get((i-1, k)) is not None and dp[(i-1, k)] < min_val:
                        min_val = dp[(i-1, k)]
                dp[(i, j)] = grid[i][j] + min_val

    return min(dp.values())

# Example usage
grid = [[1, 2], [3, 4]]
print(min_falling_path_sum(grid))  # Output: 5
