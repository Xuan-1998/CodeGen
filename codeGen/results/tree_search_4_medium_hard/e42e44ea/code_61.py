from sys import stdin

def dfs(i, j):
    if (i, j) in dp:
        return dp[(i, j)]
    
    if i < 0 or j < 0 or i >= M or j >= N:
        return float('inf')
    
    if grid[i][j] <= 0:
        return float('inf')

    result = min({ dfs(i-1, j), dfs(i, j-1) }) + grid[i][j]
    dp[(i, j)] = result
    return result

M, N = map(int, stdin.readline().split())
grid = [list(map(int, stdin.readline().split())) for _ in range(M)]

dp = {}

result = dfs(0, 0)
print(result if result != float('inf') else -1)
