import sys

N = int(sys.stdin.readline())
grid = [list(line.strip()) for line in sys.stdin.read(N).split()]

rock_free_cells = 0
mirror_able_cells = 0

for i in range(N):
    for j in range(N):
        if grid[i][j] == '.':
            rock_free_cells += 1
            mirror_able_cells += 1

for i in range(N):
    for j in range(N):
        if grid[i][j] == '.' and i > 0:
            mirror_able_cells -= 1
            for k in range(i - 1, -1, -1):
                if grid[k][j] == '#':
                    break
        if grid[i][j] == '.' and j < N - 1:
            mirror_able_cells -= 1
            for k in range(j + 1, N):
                if grid[i][k] == '#':
                    break

print(mirror_able_cells)
