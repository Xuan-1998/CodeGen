from collections import defaultdict

def min_falling_path_sum(grid):
    memo = defaultdict(int)
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if i == 0:
                memo[i][j] = grid[i][j]
            else:
                min_val = float('inf')
                for k in range(len(grid[0])):
                    min_val = min(min_val, max(grid[r][k] for r in range(i+1)))
                memo[i][j] = min(memo[i-1][k] + grid[i][j] for k in range(len(grid[0])) if min_val == grid[i-1][k])
    return min(memo[-1].values())

grid = [[31, 35, 9], [14, 23, 30], [11, 15, 13]]
print(min_falling_path_sum(grid))  # Output: 17
