def min_squares(n, m):
    # Initialize a dictionary to store the computed values.
    dp = {(i, j): 0 for i in range(1, n+1) for j in range(1, m+1)}

    # Iterate over all cells in the rectangle.
    for i in range(1, n+1):
        for j in range(1, m+1):
            # Initialize a variable to store the minimum number of squares required to tile up to cell (i, j).
            min_squares = float('inf')

            # Iterate over all possible top-left corners of a square that can be placed at cell (i, j).
            for k in range(1, i+1):
                if (i-k) * (j-1) == int(((i-k)**2 + (j-1)**2)**0.5)**2:
                    # Update the minimum number of squares required to tile up to cell (i, j).
                    min_squares = min(min_squares, dp[k-1][j-1] + 1 if k > 0 else 1)

            # Store the computed value in the dictionary.
            dp[(i, j)] = min_squares

    # Return the minimum number of squares required to tile the entire rectangle.
    return dp[(n, m)]

# Read input from stdin and print output to stdout.
if __name__ == "__main__":
    n, m = map(int, input().split())
    print(min_squares(n, m))
