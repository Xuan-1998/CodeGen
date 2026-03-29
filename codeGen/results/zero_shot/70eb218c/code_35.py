import sys

def min_operations(n, x):
    # Convert x to a string to count the number of digits
    x_str = str(x)
    len_x = len(x_str)

    if len_x >= n:
        return 0  # No operation needed if length is already equal or greater than n

    # Calculate the minimum number of operations required
    ops = n - len_x  # Initialize with the difference between n and len_x

    while len_x < n:  # Keep multiplying until the length is >= n
        x_str = str(x)  # Convert x to a string again for each iteration
        len_x = len(str(int(x)))  # Calculate the new length after multiplication
        ops += 1  # Increment the number of operations

    return ops if len_x == n else -1  # Return the minimum number of operations or -1 if impossible

n, x = map(int, input().split())
print(min_operations(n, x))
