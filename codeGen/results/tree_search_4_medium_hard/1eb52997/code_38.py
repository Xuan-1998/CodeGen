from sys import stdin

def count_mirrors(N):
    grid = [list(input()) for _ in range(N)]
    
    dp = [[0] * N for _ in range(N)]
    dp[0] = [1] * N
    
    for i in range(1, N):
        for j in range(N):
            if grid[i][j] == '.':
                dp[i][j] = (dp[i-1][j] and all(grid[k][j] == '.' for k in range(i))) or dp[i-1][j]
            else:
                dp[i][j] = 0
    
    return sum(1 for row in dp[-1] if row)

T = int(stdin.readline())
for _ in range(T):
    N = int(stdin.readline())
    print(count_mirrors(N))
