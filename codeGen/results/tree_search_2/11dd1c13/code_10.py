import sys

m = int(input())
grid = []
for _ in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

print(min_falling_path_sum(grid))
