def solve():
    T = int(input())
    for _ in range(T):
        N = int(input())
        grid = [list(input()) for _ in range(N)]
        
        dp = [[0] * N for _ in range(N)]
        dp[0] = [1 if cell == '.' else 0 for cell in grid[0]]
        
        for i in range(1, N):
            for j in range(N):
                if grid[i][j] == '.':
                    dp[i][j] = dp[i-1][j]
                    
        count = sum(dp[-1])
        print(count)
