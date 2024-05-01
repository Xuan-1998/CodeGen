from sys import stdin

# Read input grid
grid = [list(map(int, line.strip().split())) for _ in range(int(stdin.readline()))]

memo = {}

def dfs(i, j):
    if (i, j) in memo:
        return memo[(i, j)]
    
    if i == 0: 
        result = grid[i][j]
    else:
        min_sum = float('inf')
        for k in range(grid[0].index(grid[i][j])):
            result = grid[i][j] + dfs(i-1, k)
            if result < min_sum:
                min_sum = result
        for k in range(len(grid[0]) - 1, grid[0].index(grid[i][j]), -1):
            result = grid[i][j] + dfs(i-1, k)
            if result < min_sum:
                min_sum = result
        memo[(i, j)] = min_sum
    return min_sum

print(min(dfs(i, 0) for i in range(len(grid))))
