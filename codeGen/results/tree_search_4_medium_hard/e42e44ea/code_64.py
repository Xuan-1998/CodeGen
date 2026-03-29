from sys import stdin

N, M = map(int, stdin.readline().split())
grid = [list(map(int, stdin.readline().split())) for _ in range(M)]

dp = [[0] * N for _ in range(M)]

def dfs(i, j):
    if i < 0 or j < 0:
        return float('inf')
    if i == M - 1 and j == N - 1:
        return grid[i][j]
    
    if dp[i][j]:
        return dp[i][j]
    
    min_points = min(dfs(i-1, j) if i > 0 else 0, dfs(i, j-1) if j > 0 else 0) + grid[i][j]
    
    dp[i][j] = min_points
    return min_points

print(min(0, dfs(M-1, N-1)))
