from sys import stdin

N, M = map(int, stdin.readline().split())
grid = []
for _ in range(N):
    row = list(map(int, stdin.readline().split()))
    grid.append(row)

dp = [[float('inf')] * M for _ in range(N)]

def dfs(i, j):
    if i == 0 and j == 0:
        return 0
    if dp[i][j] != float('inf'):
        return dp[i][j]
    
    min_points = float('inf')
    if i > 0:
        min_points = min(min_points, dfs(i-1, j) + grid[i][j])
    if j > 0:
        min_points = min(min_points, dfs(i, j-1) + grid[i][j])
    
    dp[i][j] = min_points
    return min_points

print(dfs(N-1, M-1))
