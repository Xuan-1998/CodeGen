from collections import deque

def min_falling_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize the base case
    for j in range(n + 1):
        dp[0][j] = float('inf')
    dp[0][0] = grid[0][0]
    
    # Use a queue to perform BFS
    queue = deque([(m - 1, 0, grid[m - 1][0])])
    dp[m - 1][0] = grid[m - 1][0]
    
    while queue:
        i, j, val = queue.popleft()
        
        # Calculate the minimum sum for each cell
        if j < n:
            dp[i][j + 1] = min(dp[i][j + 1], val + grid[i][j + 1])
            queue.append((i, j + 1, dp[i][j + 1]))
        
        # Update the minimum sum for the current cell
        if i > 0:
            dp[i - 1][j] = min(dp[i - 1][j], val + grid[i - 1][j])
            queue.append((i - 1, j, dp[i - 1][j]))
    
    return dp[0][n - 1]
