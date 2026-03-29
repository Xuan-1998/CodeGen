import sys

def min_operations(n, x):
    # Convert x to a string and count its length
    x_len = len(str(x))

    if x_len >= n:
        return -1  # Impossible to make it shorter

    operations = 0
    while x_len < n:
        # Find the maximum digit that doesn't make x too long
        for y in range(10):
            new_x = x * (10 ** (n - x_len) + y)
            if len(str(new_x)) >= n:
                break
        operations += 1
        x = new_x

    return operations

# Read input from stdin
n, x = map(int, sys.stdin.readline().split())

# Call the function and print the result to stdout
print(min_operations(n, x))
