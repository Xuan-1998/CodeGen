import sys

def min_falling_path_sum(grid):
    n = len(grid)
    memo = {}

    def dfs(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        if i == n - 1:
            return grid[i][j]

        max_sum = float('-inf')
        for d in [(0, 1), (1, 0)]:
            ni, nj = i + d[0], j + d[1]
            if 0 <= ni < n and 0 <= nj < n:
                max_sum = max(max_sum, dfs(ni, nj) + grid[i][j])

        memo[(i, j)] = max_sum
        return max_sum

    min_sum = float('inf')
    for i in range(n):
        for j in range(n):
            if 0 < i:
                min_sum = min(min_sum, dfs(i - 1, j))
            else:
                min_sum = min(min_sum, dfs(i, j))

    return min_sum

# Read input from stdin
grid = []
for _ in range(int(input())):
    row = list(map(int, input().split()))
    grid.append(row)

# Calculate and print the minimum sum
print(min_falling_path_sum(grid))
