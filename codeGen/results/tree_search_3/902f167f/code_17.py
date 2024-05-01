def min_squares(n, m):
    # Initialize the table with base cases
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = i
    for j in range(m + 1):
        dp[0][j] = j

    # Fill the table in a bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            min_val = float('inf')
            for k in range(i):
                if (i - k) * (j - k) is a square number:
                    min_val = min(min_val, dp[k][j - k] + 1)
            if i is odd and j is even (or vice versa):
                min_val = min(min_val, 1)
            dp[i][j] = min_val

    # Return the minimum number of squares needed to tile the rectangle
    return dp[n][m]

# Read input from stdin
n, m = map(int, input().split())

# Print the answer to stdout
print(min_squares(n, m))
