code
T = int(input())
for _ in range(T):
    N = int(input())
    grid = [list(input()) for _ in range(N)]
    
    dp = [[0] * N for _ in range(N)]
    if grid[0][0] == '.':
        dp[0][0] = 1
    else:
        dp[0][0] = 0
    
    for i in range(1, N):
        for j in range(1, N):
            if grid[i][j] == '.'):
                dp[i][j] = dp[i-1][j] + (dp[i][j-1] if j > 0 and grid[i][j-1] == '.' else 0)
            else:
                dp[i][j] = 0
    
    print(sum(1 for row in dp if all(cell == '.' for cell in row)))
