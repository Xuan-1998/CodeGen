import sys

def min_operations(n, x):
    # Convert x to string and count the number of digits
    x_str = str(x)
    num_digits = len(x_str)

    # If x has fewer digits than n, we can't reach n by multiplying x with single-digit numbers
    if num_digits < n:
        return -1

    # Initialize the minimum number of operations
    min_ops = 0

    while True:
        # Check if x has leading zeros
        if x_str[0] == '0':
            # If yes, try to eliminate the zero by multiplying with 2 or 5
            for y in [2, 5]:
                new_x = x * y
                new_x_str = str(new_x)
                if len(new_x_str) < n:
                    x = new_x
                    x_str = new_x_str
                    min_ops += 1
        else:
            break

    # If we've reached the desired length, return the minimum number of operations
    if num_digits == n:
        return min_ops
    else:
        return -1

# Read input from stdin
n, x = map(int, sys.stdin.readline().split())

# Calculate and print the result to stdout
result = min_operations(n, x)
print(result)
