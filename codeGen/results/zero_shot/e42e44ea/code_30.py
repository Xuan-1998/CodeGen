import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

grid = []
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    grid.append(row)

def min_points_required(i, j, max_points):
    if i == N - 1 and j == M - 1:  # reached the bottom-right cell
        return max_points

    if grid[i][j] <= 0:  # invalid move (points are negative)
        return float('inf')  # return infinity to indicate no valid path

    down_points = min_points_required(i + 1, j, max_points - grid[i][j]) if i < N - 1 else float('inf')
    right_points = min_points_required(i, j + 1, max_points - grid[i][j]) if j < M - 1 else float('inf')

    return min(down_points, right_points)  # choose the path with minimum points

initial_points = min_points_required(0, 0, grid[0][0])
print(initial_points)
