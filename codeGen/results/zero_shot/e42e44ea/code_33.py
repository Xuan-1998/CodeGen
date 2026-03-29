def minInitialPoints(grid):
    M, N = len(grid), len(grid[0])
    memo = [[-1] * N for _ in range(M)]

    def dfs(i, j):
        if i == M - 1 and j == N - 1:
            return grid[i][j]
        if memo[i][j] != -1:
            return memo[i][j]

        res = float('inf')
        if i < M - 1:
            res = min(res, dfs(i + 1, j))
        if j < N - 1:
            res = min(res, dfs(i, j + 1))

        if grid[i][j] > 0:
            res = min(res, dfs(i, j) + grid[i][j])

        memo[i][j] = res
        return res

    return dfs(0, 0)

# Test the function
N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]
print(minInitialPoints(grid))
