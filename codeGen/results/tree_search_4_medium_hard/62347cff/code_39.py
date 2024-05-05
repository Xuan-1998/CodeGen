def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[float('inf')] * n for _ in range(m)]

    dp[0][0] = grid[0][0]
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return dp[m-1][n-1]

if __name__ == "__main__":
    import sys
    input = sys.stdin.read().split()
    m, n = int(input[0]), int(input[1])
    grid = []
    for _ in range(m):
        row = list(map(int, input[_+2].split()))
        grid.append(row)
    print(min_path_sum(grid))
