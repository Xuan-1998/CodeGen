import math

def min_squares(n, m):
    # Determine the minimum size of the squares
    min_size = min(n, m)

    # Calculate the maximum number of squares that can fit
    max_sqrs = (n * m) // (min_size ** 2)

    return max_sqrs

# Read input from stdin and print output to stdout
n, m = map(int, input().split())
print(min_squares(n, m))
