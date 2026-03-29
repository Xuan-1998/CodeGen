import sys

def min_initial_points(grid):
    N, M = len(grid), len(grid[0])
    
    dp = [[0 for _ in range(N)] for _ in range(M)]
    
    dp[0][0] = 1 if grid[0][0] > 0 else float('inf')
    
    for i in range(1, N):
        if grid[i][0] > 0:
            dp[i][0] = 1 + dp[i-1][0]
        else:
            break
            
    for j in range(1, M):
        if grid[0][j] > 0:
            dp[0][j] = 1 + dp[0][j-1]
        else:
            break
            
    for i in range(1, N):
        for j in range(1, M):
            if grid[i][j] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
            else:
                dp[i][j] = float('inf')
                
    return dp[M-1][N-1]

# Example usage:

if __name__ == "__main__":
    N, M = map(int, input().split())
    grid = []
    
    for _ in range(N):
        row = list(map(int, input().split()))
        grid.append(row)
        
    print(min_initial_points(grid))
