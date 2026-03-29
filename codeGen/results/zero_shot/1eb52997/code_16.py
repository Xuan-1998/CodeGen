n = int(input())
grid = [list(input()) for _ in range(n)]
empty_cells_per_row = [row.count('.') for row in grid]

valid_positions = 0
for i in range(n):
    if sum(1 for _ in range(i+1)) >= empty_cells_per_row[i]:
        valid_positions += 1

print(valid_positions)
