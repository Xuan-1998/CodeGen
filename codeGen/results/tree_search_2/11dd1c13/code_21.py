def minFallingPathSum(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]

    # Initialize the base case: when we're at the first row, just take the minimum value from that row
    for j in range(n):
        dp[0][j] = grid[0][j]

    # Fill up the rest of the dp table recursively
    for i in range(1, n):
        for j in range(n):
            if i > 0:  # Check if we're not at the first row
                min_val = float('inf')
                for k in range(n):  # Find the minimum value from the previous row
                    if k != j:  # Make sure we don't pick the same column as before
                        min_val = min(min_val, dp[i-1][k])
                dp[i][j] = grid[i][j] + min_val  # Update our current position with the minimum value from the previous row

    # Find the minimum sum among all possible paths
    return min(dp[-1])  # The last row represents all possible paths, so we just take the minimum of those


def main():
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(minFallingPathSum(grid))


if __name__ == "__main__":
    main()
