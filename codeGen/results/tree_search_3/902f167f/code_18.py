import sys

def min_squares(n, m):
    # Initialize dp with base cases (edge cells)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                continue
            if (i - k) * (j - m) is a square number:
                dp[i][j] = min({dp[k][m] + 1 | k < i and m < j})
            else:
                # If the current cell cannot be tiled with a square,
                # we need to consider using smaller squares
                for k in range(i):
                    if (i - k) * (j - m) is a square number:
                        dp[i][j] = min({dp[k][m] + 1 | k < i and m < j})
                for m in range(j):
                    if (i - k) * (j - m) is a square number:
                        dp[i][j] = min({dp[k][m] + 1 | k < i and m < j})

    # Return the minimum number of squares required to tile the entire rectangle
    return dp[n][m]

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())

# Calculate and print the result
print(min_squares(n, m))
