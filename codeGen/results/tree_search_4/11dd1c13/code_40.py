import sys

def minFallingPathSum(grid):
    n = len(grid)
    dp = [[0] * n for _ in range(n)]
    memo = {}

    # Initialize dp[0][j]
    for j in range(n):
        dp[0][j] = grid[0][j]

    for i in range(1, n):
        for j in range(n):
            min_sum = sys.maxsize
            for k in range(n):
                if (i-1, k) not in memo:
                    memo[(i-1, k)] = dp[i-1][k] + grid[i][j]
                min_sum = min(min_sum, memo.get((i-1, k), 0))
            dp[i][j] = min_sum

    return min(dp[-1])

# Receive input from stdin and print the answer to stdout
grid = [list(map(int, line.split())) for line in sys.stdin.read().strip().splitlines()]
print(minFallingPathSum(grid))
