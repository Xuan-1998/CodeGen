grid = []
for _ in range(int(input())):
    grid.append(list(map(int, input().split())))

print(min_falling_path_sum(grid))
