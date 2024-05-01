def min_falling_path(grid):
    m = len(grid)
    dp = [[0] * (m + 1) for _ in range(m)]
    memo = [[None] * (m + 1) for _ in range(m)]

    def dfs(i, j):
        if i == 0 or j == 0:
            return 0
        if memo[i][j]:
            return memo[i][j]
        min_sum = float('inf')
        for k in range(j - 1, -1, -1):
            min_sum = min(min_sum, dfs(i - 1, k) + grid[i][j])
        memo[i][j] = min_sum
        return min_sum

    ans = float('inf')
    for j in range(m):
        ans = min(ans, dfs(m - 1, j))
    return ans

grid = [list(map(int, input().split())) for _ in range(int(input()))]
print(min_falling_path(grid))
