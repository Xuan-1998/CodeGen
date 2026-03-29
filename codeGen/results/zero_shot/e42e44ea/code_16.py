def solve(grid):
    M, N = len(grid), len(grid[0])
    dp = [[0] * (N + 1) for _ in range(M + 1)]
    
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            if grid[i-1][j-1] > 0:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i-1][j-1]
    
    return dp[M][N]

if __name__ == "__main__":
    N, M = map(int, input().split())
    grid = [[int(x) for x in input().split()] for _ in range(M)]
    print(solve(grid))
