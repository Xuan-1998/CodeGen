from sys import stdin, maxsize

def min_points_to_reach_destination():
    N, M = map(int, stdin.readline().split())
    grid = [[int(x) for x in stdin.readline().split()] for _ in range(M)]
    
    dp = [[0] * (N+1) for _ in range(M+1)]
    memo = {}

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == M or j == N:
            return maxsize

        min_points = 0
        if grid[i][j] > 0 and i > 0 and dp[i-1][j] < maxsize:
            min_points = min(min_points + grid[i][j], dfs(i-1, j))
        if grid[i][j] > 0 and j > 0 and dp[i][j-1] < maxsize:
            min_points = min(min_points + grid[i][j], dfs(i, j-1))

        memo[(i, j)] = min_points
        return min_points

    min_points = dfs(0, 0)
    if min_points == maxsize:
        print(-1)  # not possible to reach the destination with positive points
    else:
        print(min_points)

min_points_to_reach_destination()
