def count_visible_cells(grid):
    N = len(grid)
    dp = [[False] * N for _ in range(N)]
    
    # Base case: First row (top) is always visible
    for col in range(N):
        dp[0][col] = True
    
    for row in range(1, N):
        for col in range(N):
            if grid[row][col] == '.':
                dp[row][col] = dp[row-1][col]
            elif grid[row][col] == '#':
                dp[row][col] = False
            else:
                # If the cell is empty (.) or the rightmost rock has been reached (#), then it's visible
                if col == N - 1 or grid[row][col+1] == '#':
                    dp[row][col] = True
    
    return sum(1 for row in dp if all(row))

# Example usage:
T = int(input())
for _ in range(T):
    N = int(input())
    grid = [list(input().strip()) for _ in range(N)]
    
    print(count_visible_cells(grid))
