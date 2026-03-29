import sys

def min_points_required(N, M, points):
    dp = [[0] * (M+1) for _ in range(N+1)]
    
    for i in range(N+1):
        for j in range(M+1):
            if i == 0 and j == 0:
                continue
            elif i > 0 and j > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + points[i-1][j-1]
            elif i > 0:
                dp[i][j] = dp[i-1][j]
            elif j > 0:
                dp[i][j] = dp[i][j-1]
            
    return dp[N][M]

N, M = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(N)]

print(min_points_required(N, M, points))
