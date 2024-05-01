def min_squares(n, m):
    # Create a 2D array to store the minimum number of squares required for each subproblem
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base case: A square of size 1 can always be tiled with 1 square
    for i in range(n + 1):
        dp[i][1] = 1

    for j in range(m + 1):
        dp[1][j] = 1

    # Fill up the dp table using dynamic programming
    for i in range(2, n + 1):
        for j in range(2, m + 1):
            if i <= j:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1
            else:
                dp[i][j] = dp[i][j - 1] + 1

    # The minimum number of squares required to tile the original rectangle is stored in the last cell of the table
    return dp[n][m]

# Read input from stdin and print output to stdout
n, m = map(int, input().split())
print(min_squares(n, m))
