grid = []
m, n = map(int, input().split())
for _ in range(m):
    row = list(map(int, input().split()))
    grid.append(row)

print(min_path_sum(grid))
