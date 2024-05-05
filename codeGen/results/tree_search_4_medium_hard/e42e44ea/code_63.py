from sys import stdin

def min_points_required():
    N, M = map(int, stdin.readline().split())
    grid = [[int(x) for x in stdin.readline().split()] for _ in range(N)]
    
    dp = [[0]*M for _ in range(N)]
    
    for i in range(1, N):
        for j in range(M):
            if grid[i][j] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
            else:
                dp[i][j] = float('inf')
    
    return dp[N-1][M-1]

print(min_points_required())
