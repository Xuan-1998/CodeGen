from collections import defaultdict

def count_mirrors(grid):
    N = len(grid)
    dp = defaultdict(int)

    for i in range(N):
        for j in range(N):
            if grid[i][j] == '.':
                rock_free_cells = 0
                for k in range(j, N):
                    if grid[i][k] == '.':
                        rock_free_cells += 1
                    else:
                        break
                dp[(i, j)] = (rock_free_cells, dp.get((i-1, j), (0,)) if i > 0 else 0)
            else:
                dp[(i, j)] = (0, 0)

    count = [0] * N
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '.':
                rock_free_cells = dp[(i, j)][0]
                for k in range(j+1, N):
                    if grid[i][k] == '.' and (dp.get((i-1, k), 0)[0] if i > 0 else 0) < rock_free_cells:
                        count[j] += 1
                        break

    return sum(count)
