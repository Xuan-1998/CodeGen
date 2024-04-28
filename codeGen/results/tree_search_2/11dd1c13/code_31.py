import sys

def min_falling_path_sum(grid):
    n = len(grid)
    dp = [[0]*n for _ in range(n)]

    # Base case: minimum sum ending at last row
    for j in range(n):
        dp[n-1][j] = grid[n-1][j]

    # Tabulation step: fill up the memoized table
    for i in range(n-2, -1, -1):
        for j in range(n):
            if i == n-2:
                dp[i][j] = grid[i][j]
            else:
                dp[i][j] = min(dp[k][j-1] for k in range(i+1)) + grid[i][j]

    # Return the minimum sum of a falling path
    return min(dp[0])

if __name__ == "__main__":
    n = int(input())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)

    print(min_falling_path_sum(grid))
