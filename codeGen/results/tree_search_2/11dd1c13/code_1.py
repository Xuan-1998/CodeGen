def min_falling_path_sum(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    for i in range(1, n):
        for j in range(n):
            prev_min = float('inf')
            for k in range(i):
                if j != grid[k][j]:
                    prev_min = min(prev_min, dp[k][grid[k][j]] + grid[i][j])
            dp[i][j] = min(dp[i-1][j] + grid[i][j], prev_min)

    return min(dp[-1])

def main():
    n = int(input())
    grid = [[int(x) for x in input().split()] for _ in range(n)]
    print(min_falling_path_sum(grid))

if __name__ == "__main__":
    main()
