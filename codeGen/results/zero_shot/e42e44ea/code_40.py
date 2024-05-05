python
def min_points_required(n, m):
    grid = []
    for _ in range(m):
        row = list(map(int, input().split()))
        grid.append(row)

    dp_table = [[float('inf')] * (n + 1) for _ in range(m + 1)]

    # Base case: 0 points required to reach the top-left cell
    dp_table[0][0] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if grid[i - 1][j - 1] > 0:
                # If the current cell has positive points,
                # we can reach it from the top-left cell with 0 points
                dp_table[i][j] = 0
            else:
                # Otherwise, we need at least one point to enter this cell
                if i == 1 and j == 1:
                    # Base case: for the top-left cell, we need at least one point
                    dp_table[i][j] = 1
                elif i > 0 and j > 0:
                    # For cells in the middle of the grid,
                    # we can reach them from either the left or above cell
                    min_points = min(dp_table[i - 1][j], dp_table[i][j - 1])
                    if min_points == float('inf'):
                        dp_table[i][j] = 0
                    else:
                        dp_table[i][j] = min_points + 1

    return dp_table[m][n]
