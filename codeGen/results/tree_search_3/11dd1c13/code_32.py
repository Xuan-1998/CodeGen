def minFallingPathSum(grid):
    n = len(grid)
    m = len(grid[0])
    
    dp = [[0] * m for _ in range(n)]
    
    # Initialize the base case
    for j in range(m):
        dp[0][j] = grid[0][j]
        
    for i in range(1, n):
        for j in range(m):
            # Calculate the minimum sum of a falling path with non-zero shifts
            min_sum = float('inf')
            for k in range(m):
                if k != j:  # Ensure we consider all possible columns
                    min_sum = min(min_sum, dp[i-1][k] + grid[i][j])
            dp[i][j] = min_sum
    
    return min(dp[-1])

# Read the input grid from standard input
grid = []
for _ in range(int(input())):
    row = list(map(int, input().split()))
    grid.append(row)

print(minFallingPathSum(grid))
