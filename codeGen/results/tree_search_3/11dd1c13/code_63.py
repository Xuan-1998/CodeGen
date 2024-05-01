def min_sum_of_falling_path(i, j):
    if (i, j) in memo:
        return memo[(i, j)]

    if i == 0:
        return 0

    min_sum = float('inf')
    for k in range(len(grid[0])):
        if grid[i-1][k] != grid[i][j]:
            min_sum = min(min_sum, min_sum_of_falling_path(i-1, k) + grid[i][j])
            memo[(i, j)] = min_sum
            return min_sum

grid = [list(map(int, input().split())) for _ in range(int(input()))]
memo = {}
print(min_sum_of_falling_path(len(grid)-1, len(grid[0])-1))
