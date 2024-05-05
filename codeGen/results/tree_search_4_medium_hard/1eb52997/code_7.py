import sys

T = int(input())
for _ in range(T):
    N = int(input())
    grid = [list(input()) for _ in range(N)]
    
    dp = [[0] * N for _ in range(N)]
    
    def can_see_east(i, j):
        if i < 0 or j < 0:
            return False
        if grid[i][j] == '#':
            return False
        if dp[i][j]:
            return True
        res = can_see_east(i-1, j)
        dp[i][j] = res and (grid[i][j] == '.' or dp[i-1][j])
        return dp[i][j]
    
    result = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '.':
                result += can_see_east(i, j)
    print(result)
