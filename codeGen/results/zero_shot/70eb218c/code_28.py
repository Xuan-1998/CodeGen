import sys

# Read input from stdin
n, x = map(int, input().split())

# Calculate the current number of digits in the decimal representation of x
current_digits = len(str(x))

# If the current number of digits is already equal to n, return 0
if current_digits == n:
    print(0)
else:
    # Calculate the minimum number of operations required
    min_operations = n - current_digits

    # Print the result to stdout
    print(min_operations)
