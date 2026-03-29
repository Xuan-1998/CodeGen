def count_mirror_options():
    T = int(input())
    for _ in range(T):
        N = int(input())
        dp = [[0]*N for _ in range(N)]
        
        # Pre-compute visibility for all rows
        for i in range(N):
            for j in range(N):
                if grid[i][j] == '.':
                    if all(grid[k][j] == '.' for k in range(i+1)):
                        dp[i][j] = 1
                    else:
                        dp[i][j] = max(dp[i-1][j], dp[i][j])
        
        # Compute total number of possible options
        result = sum(dp[-1])
        print(result)

count_mirror_options()
