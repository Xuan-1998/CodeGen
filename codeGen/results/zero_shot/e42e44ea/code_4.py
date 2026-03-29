import sys

def min_points(i, j):
    if i == N - 1 and j == M - 1:  # destination cell
        return 0

    min_points_needed = float('inf')  # initialize to infinity

    if grid[i][j] > 0:
        down_points = min_points(i + 1, j)
        right_points = min_points(i, j + 1)

        if down_points != float('inf') and right_points != float('inf'):
            min_points_needed = min(down_points, right_points) + grid[i][j]

    return min_points_needed

N, M = map(int, input().split())  # read grid size from stdin
grid = [[int(x) for x in input().split()] for _ in range(N)]

print(min_points(0, 0))  # print the minimum initial points required to reach the destination cell
