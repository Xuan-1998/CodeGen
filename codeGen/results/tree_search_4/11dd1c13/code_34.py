import sys

def dp(i, j):
    if i == 0:
        return grid[i][j]
    elif (i, j) in memo:
        return memo[(i, j)]
    else:
        min_sum = float('inf')
        for k in range(n):  # iterate over all columns
            if k != j:  # ensure we're not choosing the same column as before
                min_sum = min(min_sum, dp(i-1, k)) + grid[i][j]
        memo[(i, j)] = min_sum
        return min_sum

n = int(input())  # get the size of the square grid
grid = []
for i in range(n):
    row = list(map(int, input().split()))  # read the grid from stdin
    grid.append(row)

memo = {}

min_sum = 0
for j in range(n):  # iterate over all columns
    min_sum += dp(0, j)  # start the dynamic programming from the first row

print(min_sum)  # print the minimum sum of a falling path with non-zero shifts
