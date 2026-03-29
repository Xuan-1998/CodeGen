import sys

def min_operations(n, x):
    # Convert x to string for easier manipulation
    str_x = str(x)
    
    # Calculate the minimum number of operations required
    ops = 0
    while len(str_x) < n:
        max_digit = int("9" * (n - len(str_x)))
        if x <= max_digit:
            return -1  # impossible to reach n
        x *= max_digit
        ops += 1
    
    return ops

# Read input from stdin
n, x = map(int, sys.stdin.readline().split())

# Calculate and print the minimum number of operations
print(min_operations(n, x))
