import sys

def can_place_mirror(grid):
    N = len(grid)
    dp = [[0] * N for _ in range(N)]

    # Initialize base case: edge of grid has no rocks
    for j in range(N):
        dp[0][j] = 1

    for i in range(1, N):
        for j in range(N):
            if grid[i][j] == '.':
                # No rock at this cell; check cells to the East
                dp[i][j] = all(dp[k][j] for k in range(i))
            else:
                # Rock at this cell; no mirror can be placed
                dp[i][j] = 0

    return sum(1 for row in dp[-1] if row)

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        grid = [list(input()) for _ in range(N)]
        print(can_place_mirror(grid))

if __name__ == "__main__":
    main()
