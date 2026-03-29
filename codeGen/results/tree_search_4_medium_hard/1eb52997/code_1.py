def count_mirror_positions():
    T = int(input())
    for _ in range(T):
        N = int(input())
        grid = [list(input().strip()) for _ in range(N)]
        
        dp = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if grid[i][j] == '.':
                    for k in range(i+1, N):
                        if '#' not in grid[k][j:]:
                            dp[i][j] = 1
                            break
        
        total_options = sum(1 for row in dp for cell in row if cell)
        
        print(total_options)

count_mirror_positions()
