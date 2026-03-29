def count_mirrors(grid):
    N = len(grid)
    dp = [[0] * (N+1) for _ in range(N+1)]

    # Base case: edge of grid or no rocks blocking line of sight
    for j in range(N+1):
        dp[0][j] = 1

    for i in range(1, N+1):
        for j in range(N+1):
            if grid[i-1][j-1] == '.':
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + (i > 0)
            else:
                dp[i][j] = 0

    # Sum of values in last row is the answer
    return sum(dp[-1])

T = int(input())
for _ in range(T):
    N = int(input())
    grid = [list(input()) for _ in range(N)]
    print(count_mirrors(grid))
