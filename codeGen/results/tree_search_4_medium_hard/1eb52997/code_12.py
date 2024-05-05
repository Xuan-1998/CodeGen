def count_mirrors(grid):
    N = len(grid)
    dp = [[False]*N for _ in range(N)]
    
    # Fill the table row by row from top to bottom
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '.' and (j == N-1 or grid[i][j+1] == '.'):
                dp[i][j] = True
    
    return sum([1 for row in dp for _ in row].count(True))

T = int(input())
for _ in range(T):
    N = int(input())
    grid = [list(input().strip()) for _ in range(N)]
    print(count_mirrors(grid))
