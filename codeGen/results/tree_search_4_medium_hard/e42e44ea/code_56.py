def minInitialPoints(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * (n+1) for _ in range(m+1)]

    # Initialize base cases
    for i in range(m+1):
        dp[i][0] = 0 if i == 0 else float('inf')
    for j in range(n+1):
        dp[0][j] = 0 if j == 0 else float('inf')

    for i in range(1, m+1):
        for j in range(1, n+1):
            # Transition relation
            if grid[i-1][j-1] > 0:
                dp[i][j] = min(dp[i-1][j][grid[i-1][j-1]], dp[i][j-1][grid[i-1][j-1]]) + grid[i-1][j-1]
            else:
                dp[i][j] = float('inf')

    # Perform a depth-first search to find the minimum initial points
    min_points = float('inf')
    stack = [(m, n)]
    while stack:
        i, j = stack.pop()
        if i > 0 and j > 0:
            if grid[i-1][j-1] > 0:
                new_points = dp[i][j] - grid[i-1][j-1]
                if new_points < min_points:
                    min_points = new_points
                stack.append((i-1, j-1))
            elif i > 0 and j > 0:
                stack.append((i-1, j))
                stack.append((i, j-1))

    return min_points

# Example usage:
grid = [[3,2,1], [1,5,3], [1,8,2]]
print(minInitialPoints(grid))  # Output: 7
