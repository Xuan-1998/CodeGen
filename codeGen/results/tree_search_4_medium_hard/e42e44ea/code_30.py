import sys
from typing import List

def min_points(grid: List[List[int]]) -> int:
    M, N = len(grid), len(grid[0])
    
    # Initialize dp table with infinity for all cells except the top row and left column
    dp = [[float('inf')] * N for _ in range(M)]
    dp[0] = grid[0]
    for j in range(N):
        dp[j][0] = grid[0][j]
    
    # Fill up the dp table using state transition function
    for i in range(1, M):
        for j in range(1, N):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[M-1][N-1]

if __name__ == '__main__':
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(M)]
    print(min_points(grid))
