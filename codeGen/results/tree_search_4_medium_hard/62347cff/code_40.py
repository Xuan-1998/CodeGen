# Initialize the dp array with infinity for all cells
dp = [[float('inf') for _ in range(n)] for _ in range(m)]

# Base case: The minimum sum of all numbers along a path ending at the top or left boundary is 0
for i in range(m):
    dp[i][0] = grid[i][0]
for j in range(n):
    dp[0][j] = grid[0][j]

# Fill the dp array using the optimal substructure property
for i in range(1, m):
    for j in range(1, n):
        # The minimum sum of all numbers along a path ending at cell [i][j] is the minimum of:
        # 1. The minimum sum of all numbers along a path ending at the cell above it (dp[i-1][j]) plus the value at the current cell
        # 2. The minimum sum of all numbers along a path ending at the cell to its left (dp[i][j-1]) plus the value at the current cell
        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

# The final answer is stored at dp[m-1][n-1], which represents the minimum sum of all numbers along the path from the top left corner to the bottom right corner of the grid
print(dp[m-1][n-1])
