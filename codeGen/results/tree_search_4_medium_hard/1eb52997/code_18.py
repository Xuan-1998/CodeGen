def count_mirrors(grid):
    N = len(grid)
    dp = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if grid[i][j] == '.':
                if all(grid[k][j] == '.' for k in range(i+1, N)):
                    dp[i][j] = dp[i-1][j] if i > 0 else 1
                else:
                    dp[i][j] = 0

    total_valid_placements = 0
    for i in range(N):
        for j in range(N):
            total_valid_placements += dp[i][j]

    return total_valid_placements

def main():
    T = int(input())  # Read the number of test cases
    for _ in range(T):
        N = int(input())
        grid = [list(input().strip()) for _ in range(N)]
        print(count_mirrors(grid))

if __name__ == "__main__":
    main()
