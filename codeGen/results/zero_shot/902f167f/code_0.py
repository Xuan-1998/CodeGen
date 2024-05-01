import sys

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())

# Initialize a 2D array to store the minimum number of squares for each sub-rectangle
dp = [[0] * (m + 1) for _ in range(n + 1)]

# Fill up the dp table
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # If the current sub-rectangle is a square, try to fill it with as few squares as possible
        if i ** 0.5 == int(i ** 0.5) and j ** 0.5 == int(j ** 0.5):
            dp[i][j] = min(dp[i - k][j - k] + (k ** 2), k)
        # If the current sub-rectangle is not a square, try to fill it with as few rectangles as possible
        else:
            for k in range(1, min(i, j) + 1):
                dp[i][j] = min(dp[i][j], dp[i - k][j] + dp[i][j - k])
