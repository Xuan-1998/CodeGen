import sys

def count_mirrors(n):
    dp = [[0]*n for _ in range(n)]
    
    # Base cases
    for j in range(n):
        dp[0][j] = 1 if (j == 0 or grid[0][j-1] != '.') else 0
    
    for i in range(1, n):
        for j in range(n):
            if grid[i][j] == '.':
                if j == 0:  # left border
                    dp[i][j] = dp[i-1][j]
                elif j == n-1:  # right border
                    dp[i][j] = dp[i-1][n-2]
                else:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
            else:  # rock
                dp[i][j] = 0
    
    return sum(1 for row in dp if all(cell == '1' for cell in row))

T = int(input())
for _ in range(T):
    n = int(input())
    grid = [list(input().strip()) for _ in range(n)]
    
    print(count_mirrors(n))
