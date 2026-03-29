import sys

def min_operations(n, x):
    # Convert integer x to string for easy manipulation of digits
    x_str = str(x)

    # Calculate the current length of decimal representation of x
    curr_len = len(x_str)

    if curr_len >= n:
        return 0

    min_ops = float('inf')  # Initialize minimum operations as infinity

    # Loop through each digit in x's decimal representation
    for i, d in enumerate(x_str):
        # Create a new string by prepending zeros to the left of the current digit
        new_x_str = '0' * (n - curr_len + i) + d
        
        # Convert the new string back to an integer and calculate its length
        new_x = int(new_x_str)
        new_len = len(str(new_x))

        # Calculate the number of operations required to reach the desired length n
        ops = new_len - n

        # Update minimum operations if the current operation count is less
        min_ops = min(min_ops, ops)

    if min_ops == float('inf'):
        return -1  # If no possible operations found, return -1

    return min_ops

# Read input from stdin and process
n, x = map(int, sys.stdin.readline().split())
print(min_operations(n, x))
