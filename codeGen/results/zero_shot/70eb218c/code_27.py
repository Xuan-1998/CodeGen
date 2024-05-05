import sys

def min_operations(n, x):
    # Convert x to a string and count its length
    x_str = str(x)
    current_len = len(x_str)

    if current_len == n:
        return 0  # No operations needed!

    # Calculate the maximum possible length of x's decimal representation
    max_len = int('9' * (n - 1))

    # Check if it's impossible to make the length equal to n
    if current_len > max_len:
        return -1

    # Find the minimum number of operations required
    diff = n - current_len
    operations = 0

    while diff > 0:
        # Find the largest digit y such that x * 10^y < 10^n and x * 10^y >= current_len + 1
        for y in range(diff, 0, -1):
            if int('9' * (n - 1)) // (10 ** y) >= current_len + 1:
                break

        # Apply the operation: x = x * 10^y
        operations += 1
        diff -= y

    return operations

# Read input from stdin
n, x = map(int, sys.stdin.readline().split())

# Calculate and print the minimum number of operations
print(min_operations(n, x))
