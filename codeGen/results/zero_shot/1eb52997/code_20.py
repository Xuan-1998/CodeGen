import sys

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    grid = [['.' * N] * N]
    count = 0
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '.':  # empty cell
                is_east_unobstructed = True
                for k in range(i+1, N):
                    if grid[k][j] == '#':  # rock blocking line of sight
                        is_east_unobstructed = False
                        break
                if is_east_unobstructed:
                    count += 1
    print(count)
