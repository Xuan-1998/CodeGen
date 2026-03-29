import sys

def min_initial_points(N, M, grid):
    dp = [[sys.maxsize] * M for _ in range(N)]
    dp[0][0] = 0
    
    for i in range(1, N):
        dp[i][0] = 0
    for j in range(1, M):
        dp[0][j] = 0
    
    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[N-1][M-1]

# Read input from stdin
N, M = map(int, input().split())
grid = [[int(x) for x in input().split()] for _ in range(N)]

# Call the function and print the result to stdout
print(min_initial_points(N, M, grid))
