import sys
from collections import defaultdict

def count_mirror_placements(grid):
    N = len(grid)
    dp = [[False] * N for _ in range(N)]
    
    # Base case: No rocks on the edge, so mirror can be placed
    for i in range(N):
        dp[i][0] = True
        dp[0][i] = True
    
    memo = defaultdict(bool)
    
    def dfs(row, col):
        if (row, col) in memo:
            return memo[(row, col)]
        
        # Base case: No rocks at this position, so mirror can be placed
        if grid[row][col] == '.':
            dp[row][col] = True
            for i in range(1, N):
                if grid[row][i] == '#':
                    break
                dp[row][i] = dfs(row, i)
            return any(dp[row][i] for i in range(N))
        
        # If rock is present, recursively check right side cells until first rock found
        else:
            memo[(row, col)] = False
            for i in range(1, N):
                if grid[row][i] == '#':
                    break
                dp[row][i] = dfs(row, i)
            return any(dp[row][i] for i in range(N))
    
    count = 0
    for row in range(N):
        for col in range(N):
            count += dfs(row, col)
    
    print(count)

T = int(input())
for _ in range(T):
    N = int(input())
    grid = [list(input()) for _ in range(N)]
    count_mirror_placements(grid)
