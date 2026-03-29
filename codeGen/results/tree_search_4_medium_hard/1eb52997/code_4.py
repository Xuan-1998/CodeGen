import sys

def count_mirrors(grid):
    N = len(grid)
    dp = [[0] * N for _ in range(N)]
    memo = {}

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]
        if grid[i][j] == '#':
            return 0
        count = 1
        for k in range(j+1, N):
            if grid[i][k] == '.':
                count += dfs(i, k)
            else:
                break
        memo[(i, j)] = count
        return count

    total = 0
    for i in range(N):
        for j in range(N):
            if dp[i][j] == 1:
                total += dfs(i, j)

    return total

T = int(input())
for _ in range(T):
    N = int(input())
    grid = [input() for _ in range(N)]
    print(count_mirrors(grid))
