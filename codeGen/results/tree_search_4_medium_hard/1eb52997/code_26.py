from collections import defaultdict

def count_mirrors(grid):
    T, N = map(int, input().split())
    memo = defaultdict(int)

    def dfs(i, j):
        if (i, j) not in memo:
            if i == 0 or grid[i][j] == '.':
                memo[(i, j)] = 1
            elif j > 0 and grid[i][j-1] == '.':
                memo[(i, j)] = dfs(i, j-1)
            else:
                memo[(i, j)] = 0
        return memo[(i, j)]

    for _ in range(T):
        N = int(input())
        grid = [list(input().strip()) for _ in range(N)]
        total_mirrors = sum(dfs(i, j) for i in range(N) for j in range(N))
        print(total_mirrors)

count_mirrors([])
