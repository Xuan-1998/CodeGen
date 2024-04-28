grid = []
while True:
    try:
        row = list(map(int, input().split()))
        grid.append(row)
    except EOFError:
        break
min_sum = float('inf')
for i in range(len(grid[0])):
    for j in range(len(grid[0])):
        sum_path = 0
        last_col = None
        for k in range(len(grid)):
            if k == len(grid) - 1 or abs(i-j) != 0:
                if last_col is not None and i == last_col:
                    continue
                sum_path += grid[k][j]
                last_col = j
        min_sum = min(min_sum, sum_path)
print(min_sum)
