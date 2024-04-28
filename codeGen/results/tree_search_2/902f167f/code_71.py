import sys

# Memoization dictionary to store computed dp[i][j] values
dp = {}

def min_squares(n, m):
    if (n, m) not in dp:
        if n == 0 or m == 0:
            dp[(n, m)] = 0
        elif n <= 1 and m <= 1:
            dp[(n, m)] = 0
        else:
            # Check if the rectangle can be tiled with a single square of size min(n, m)
            if n % min(n, m) == 0 and m % min(n, m) == 0:
                dp[(n, m)] = 1
            else:
                # Calculate the minimum number of squares that tile the top part of the rectangle (of size n-1 x m)
                top_part_squares = 1 + min_squares(n - 1, m)
                
                # Calculate the minimum number of squares that tile the left part of the rectangle (of size n x m-1)
                left_part_squares = 1 + min_squares(n, m - 1)
                
                # Choose the minimum number of squares between the top and left parts
                dp[(n, m)] = 1 + min(top_part_squares, left_part_squares)

    return dp[(n, m)]

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())

# Calculate and print the minimum number of integer-sided squares that tile the given rectangle
print(min_squares(n, m))
