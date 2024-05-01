def minFallingPathSum(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == 0:
                dp[i][j] = grid[i][j]
            else:
                min_val = float('inf')
                for k in range(n):
                    if k != j:
                        min_val = min(min_val, dp[i-1][k] + grid[i][j])
                dp[i][j] = min_val
    
    return min(dp[-1])

if __name__ == "__main__":
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    
    print(minFallingPathSum(grid))
