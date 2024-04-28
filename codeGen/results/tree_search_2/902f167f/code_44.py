def min_squares(n, m):
    # Initialize dp with zeros
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base case: one square of size 1x1 is always needed to tile a rectangle of size 1x1
    dp[1][1] = 1

    for i in range(2, n + 1):
        for j in range(2, m + 1):
            # For each possible square side length k from 1 to min(i, j)
            for k in range(1, min(i, j) + 1):
                # The minimum number of squares that tile the current rectangle
                # is one more than the minimum number of squares needed to tile
                # the sub-rectangle with size (i-k) x (j-k)
                dp[i][j] = min(dp[i][j], dp[i - k][j - k] + 1)

    return dp[n][m]

# Read input from stdin
n, m = map(int, input().split())

print(min_squares(n, m))
