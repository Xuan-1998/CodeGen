def minInitialPoints(grid):
    N, M = len(grid), len(grid[0])
    dp = [[0] * M for _ in range(N)]

    # Initialize the top row and left column
    for i in range(N):
        if grid[i][0] > 0:
            dp[i][0] = grid[i][0]
        else:
            break

    for j in range(M):
        if grid[0][j] > 0:
            dp[0][j] = grid[0][j]
        else:
            break

    # Fill up the rest of the DP table
    for i in range(1, N):
        for j in range(1, M):
            if grid[i][j] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            else:
                break

    return dp[-1][-1]

# Example usage
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
print(minInitialPoints(grid))
