def min_squares(n, m):
    # Initialize memoization table
    dp = [[float('inf')] * (m + 1) for _ in range(n + 1)]

    # Base case: A single square of size 0x0
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i > 0 and j > 0:
                # Check all possible squares that can be placed diagonally
                min_squares = float('inf')
                for k in range(min(i, j) + 1):
                    # Calculate the number of squares needed to tile the subrectangle
                    min_squares = min(min_squares, dp[i - k][j - k] + (i // k) * (j // k))
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1 if i > 0 and j > 0 else min_squares

    return dp[n][m]
