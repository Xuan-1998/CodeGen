from sys import stdin

# Read input from stdin
N, M = map(int, stdin.readline().split())
grid = []
for _ in range(N):
    row = list(map(int, stdin.readline().split()))
    grid.append(row)

# Initialize DP table with initial values (0 for top-left cell)
dp_table = [[float('inf')] * M for _ in range(N)]
dp_table[0][0] = 0

# Fill DP table
for i in range(N):
    for j in range(M):
        if i > 0:
            dp_table[i][j] = min(dp_table[i-1][j], dp_table[i][j]) + grid[i][j]
        if j > 0:
            dp_table[i][j] = min(dp_table[i][j-1], dp_table[i][j]) + grid[i][j]

# Find minimum points required to reach bottom-right cell
min_points = float('inf')
for i in range(N):
    for j in range(M):
        if i == N - 1 and j == M - 1:
            min_points = min(min_points, dp_table[i][j])

print(min_points)
