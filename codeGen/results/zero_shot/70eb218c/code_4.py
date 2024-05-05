import sys

# Read input from stdin
n, x = map(int, sys.stdin.readline().split())

# Calculate the initial length of decimal representation of x
initial_length = len(str(x))

# If the initial length is already equal to n, output 0
if initial_length == n:
    print(0)
else:
    # Initialize the number of operations
    operations = 0

    # Loop until the length of decimal representation of x reaches or exceeds n
    while initial_length < n:
        # Find the maximum digit that can be multiplied with x to make its length increase by 1
        max_digit = int(str(x)[-1]) + 1

        # Multiply x by the maximum digit and update x and initial_length
        x *= max_digit
        initial_length += 1

        # Increment the number of operations
        operations += 1

    # Output the minimum number of operations
    print(operations)
