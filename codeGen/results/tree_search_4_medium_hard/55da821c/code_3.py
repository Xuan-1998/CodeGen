import sys

def min_replant(n, m):
    # Initialize the 2D table with zeros
    dp = [[0] * (n + 1) for _ in range(m)]

    # Initialize the first row to represent the base case: all plants are in their correct section
    for i in range(1, n + 1):
        dp[0][i] = i

    # Fill in the rest of the table using dynamic programming
    for i in range(1, m):
        for j in range(i, n + 1):
            if dp[i - 1][j] == j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1] + 1)

    # The final answer is the last cell of the bottom row
    return dp[m - 1][n]

# Receive input from stdin and print the output to stdout
n, m = map(int, sys.stdin.readline().split())
print(min_replant(n, m))
