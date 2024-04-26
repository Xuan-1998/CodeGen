import sys

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
grid = [sys.stdin.readline().strip() for _ in range(n)]

# Calculate the number of empty cells and their positions
empty_cells = []
for i in range(n):
    for j in range(m):
        if grid[i][j] == '.':
            empty_cells.append((i, j))

# Initialize the sum of distances and count of pairs
sum_of_distances = 0
count_of_pairs = 0

# Calculate the sum of Manhattan distances between all pairs of empty cells
for i in range(len(empty_cells)):
    for j in range(i + 1, len(empty_cells)):
        x1, y1 = empty_cells[i]
        x2, y2 = empty_cells[j]
        sum_of_distances += abs(x1 - x2) + abs(y1 - y2)
        count_of_pairs += 1

# Calculate the average lifespan
average_lifespan = sum_of_distances / count_of_pairs if count_of_pairs != 0 else 0

# Print the average lifespan to stdout with an accuracy of at least 6 decimal places
print(f"{average_lifespan:.6f}")
