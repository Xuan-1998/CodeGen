def minFallingPathSum(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    # base case
    dp[0][j] = grid[0][j]
    
    # fill up the table using dynamic programming and memoization
    for i in range(1, n):
        for j in range(n):
            min_sum = float('inf')
            for k in range(n):
                if j != k:
                    min_sum = min(min_sum, dp[i-1][k] + grid[i][j])
            dp[i][j] = min_sum

    # find the minimum sum of a falling path
    return min(dp[-1])

# receive input from stdin
n = int(input())
grid = []
for _ in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

print(minFallingPathSum(grid))
