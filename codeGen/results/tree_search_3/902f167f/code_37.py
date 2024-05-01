import math

def min_squares(n, m):
    # Initialize dynamic programming arrays
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        square_root = int(math.sqrt(i))
        if square_root ** 2 == i:
            dp[i] = 1
        else:
            dp[i] = min(dp[j] + 1 for j in range(square_root, i))

    # Calculate the minimum number of squares required to tile each row
    row_squares = [0] * (m + 1)
    for j in range(1, m + 1):
        square_root = int(math.sqrt(j))
        if square_root ** 2 == j:
            row_squares[j] = 1
        else:
            row_squares[j] = min(row_squares[k] + 1 for k in range(square_root, j))

    # Return the minimum number of squares required to tile the entire rectangle
    return dp[n] * row_squares[m]

# Read input from standard input
n, m = map(int, input().split())

# Print the output to standard output
print(min_squares(n, m))
