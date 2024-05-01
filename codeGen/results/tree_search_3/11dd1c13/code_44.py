from itertools import product

def solve():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    
    dp = [[0]*n for _ in range(n)]
    
    for i in range(1, n):
        for j in range(n):
            min_sum = float('inf')
            for shift in product(range(-i+1), range(i)):
                if all(grid[i-1][k] != grid[i-1-shift[0]][k+shift[1]] for k in range(min(j-shift[1], n-j+shift[1]))):
                    min_sum = min(min_sum, dp[i-1][min(max(0, j-shift[1]), n-1)] + grid[i][j])
            dp[i][j] = min_sum
    
    return min(dp[-1])

print(solve())
