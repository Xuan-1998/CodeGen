def place_mirrors(grid):
    N = len(grid)
    dp = [[0]*N for _ in range(N)]

    # Correct edge cases
    for j in range(N):
        if grid[0][j] == '.':
            dp[0][j] = 1
    for i in range(N):
        if grid[i][0] == '.':
            dp[i][0] = 1

    for i in range(1, N):
        for j in range(1, N):
            if grid[i][j] == '.' and grid[i][j-1] == '.':
                dp[i][j] = 1
            elif grid[i][j] == '.' and grid[i-1][j] == '.':
                dp[i][j] = 1

    return sum([sum(row) for row in dp])

T = int(input())
for _ in range(T):
    N = int(input())
    grid = [list(input()) for _ in range(N)]
    print(place_mirrors(grid))
