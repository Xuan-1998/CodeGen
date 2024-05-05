import sys

def count_mirror_placement(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    # Initialize the base case: if the cell is empty, a mirror can be placed.
    for j in range(n):
        dp[0][j] = 1 if grid[0][j] == '.' else 0

    # Fill up the dynamic programming table
    for i in range(1, n):
        for j in range(n):
            if grid[i][j] == '.':
                dp[i][j] = (dp[i-1][j] + sum(dp[k][j] for k in range(i))) % 2
            else:
                dp[i][j] = 0

    # Count the number of mirror placement options
    count = sum(1 for i in range(n) if dp[n-1][i])
    return count

t = int(input())
for _ in range(t):
    n = int(input())
    grid = [list(input()) for _ in range(n)]
    print(count_mirror_placement(grid))
