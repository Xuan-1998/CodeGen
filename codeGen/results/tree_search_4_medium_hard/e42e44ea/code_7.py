import sys

def f(N, M):
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    dp = [[0] * M for _ in range(N)]
    dp[0][0] = grid[0][0]
    
    for i in range(1, N):
        if grid[i][0] > 0:
            dp[i][0] = dp[i-1][0] + grid[i][0]
        else:
            break
    
    for j in range(1, M):
        if grid[0][j] > 0:
            dp[0][j] = dp[0][j-1] + grid[0][j]
        else:
            break
    
    for i in range(1, N):
        for j in range(1, M):
            if grid[i][j] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            else:
                break
    
    return dp[N-1][M-1]

N, M = map(int, input().split())
print(f(N, M))
