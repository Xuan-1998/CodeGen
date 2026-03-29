import sys

def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    prev = [[None] * n for _ in range(m)]

    # Base case: bottom right corner
    dp[m-1][n-1] = grid[m-1][n-1]

    # Fill up the dynamic programming table
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            elif i > 0 and j == 0:
                dp[i][j] = dp[i-1][j] + grid[i][j]
                prev[i][j] = (i-1, j)
            elif i == 0 and j > 0:
                dp[i][j] = dp[i][j-1] + grid[i][j]
                prev[i][j] = (i, j-1)
            else:
                if dp[i-1][j] < dp[i][j-1]:
                    dp[i][j] = dp[i-1][j] + grid[i][j]
                    prev[i][j] = (i-1, j)
                else:
                    dp[i][j] = dp[i][j-1] + grid[i][j]
                    prev[i][j] = (i, j-1)

    # Reconstruct the optimal path
    path_sum = 0
    i, j = m-1, n-1
    while i > 0 or j > 0:
        if i > 0 and j > 0:
            if dp[i-1][j] < dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        elif i > 0:
            i -= 1
        else:
            j -= 1
        path_sum += grid[i][j]

    return path_sum

# Test the function
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(min_path_sum(grid))  # Output: 25
