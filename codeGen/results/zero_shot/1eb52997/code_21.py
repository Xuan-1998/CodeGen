N = int(input())
grid = []
for _ in range(N):
    row = list(input().strip())
    grid.append(row)

T = int(input())
for _ in range(T):
    N = int(input())
    grid = []
    for _ in range(N):
        row = list(input().strip())
        grid.append(row)
    print(count_mirrors(grid))

def count_mirrors(grid):
    count = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '.':
                is_clear = True
                for k in range(i, N):
                    if grid[k][j] == '#':
                        is_clear = False
                        break
                if is_clear:
                    count += 1
    return count
