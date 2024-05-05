import sys

def min_operations(n, x):
    # Convert x to string for easier manipulation
    x_str = str(x)

    # Calculate the current length of x
    curr_len = len(x_str)

    # If x is already n digits long, return 0 operations
    if curr_len == n:
        return 0

    # Initialize the operation count
    ops = 0

    # Loop until we reach the desired length
    while curr_len < n:
        # Find the most significant digit in x_str
        most_sig_digit = int(x_str[0])

        # Multiply x by this digit to make it longer
        new_x = int(str(most_sig_digit) * (curr_len + 1))

        # Update the operation count and current length
        ops += 1
        curr_len += 1

        # Update x_str for the next iteration
        x_str = str(new_x)

    return ops

# Read input from stdin
n, x = map(int, sys.stdin.readline().split())

# Print the result to stdout
print(min_operations(n, x))
