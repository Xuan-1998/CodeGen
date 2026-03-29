def count_visible_cells(grid):
    N = len(grid)
    visible = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if grid[i][j] == '.':
                # Check visibility from the cell to the East
                for k in range(i + 1, N):
                    if grid[k][j] == '#':
                        break
                else:
                    visible[i][j] = True

    return sum(1 for row in visible if all(row))

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        grid = [list(input()) for _ in range(N)]
        print(count_visible_cells(grid))

if __name__ == "__main__":
    main()
