import sys
from collections import defaultdict

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

memo = defaultdict(lambda: defaultdict(sys.maxsize))

def dp(i, j):
    if i == n - 1:
        return grid[i][j]
    
    if memo[i][j] != sys.maxsize:
        return memo[i][j]
    
    min_sum = sys.maxsize
    for k in range(j+1, len(grid[0])):
        min_sum = min(min_sum, dp(i-1, k) + grid[i][j])
    
    memo[i][j] = min_sum
    return min_sum

print(dp(0, 0))
