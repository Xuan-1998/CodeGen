def count_mirrors(grid):
    N = len(grid)
    dp = [[0] * N for _ in range(N)]

    # Initialize the base case: the first row is always visible
    for j in range(N):
        if grid[0][j] == '.':
            dp[0][j] = 1

    for i in range(1, N):
        for j in range(N):
            if grid[i][j] == '.':
                # Check the visibility of the cell to its right
                visible = all(grid[i][k] == '.' for k in range(j+1, N))
                dp[i][j] = 1 if visible else 0

    return sum(dp[i].count(1) for i in range(N))

T = int(input())
for _ in range(T):
    N = int(input())
    grid = [list(input().strip()) for _ in range(N)]
    print(count_mirrors(grid))
