N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(M)]

min_points = float('inf')
for i in range(M):
    for j in range(N):
        if grid[i][j] > 0:  # only consider cells with positive points
            min_points = min(min_points_required(i, j, grid), min_points)

print(min_points)
