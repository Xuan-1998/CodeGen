def get_mirror_placements(grid):
    N = len(grid)
    dp = [[0] * N for _ in range(N)]

    for row in range(N):
        for col in range(N):
            if grid[row][col] == '.':
                if col + 1 < N and grid[row][col+1] == '.':
                    dp[row][col] += 1
            elif col + 1 < N and grid[row][col+1] == '.':
                dp[row][col] += 1

    return sum(sum(row) for row in dp)

T = int(input())
for _ in range(T):
    N = int(input())
    grid = [list(input()) for _ in range(N)]
    print(get_mirror_placements(grid))
