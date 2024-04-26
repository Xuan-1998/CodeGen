import sys

def min_operations_to_beautiful(s, l, r):
    # Initialize the number of operations to 0
    operations = 0
    # Iterate over the substring from l to r-1 (since we compare with the next character)
    for i in range(l, r):
        # If the current character is the same as the next one, we need an operation
        if s[i] == s[i + 1]:
            operations += 1
    return operations

# Read input from stdin
n, m = map(int, sys.stdin.readline().split())
s = sys.stdin.readline().strip()

# Process each query
for _ in range(m):
    l, r = map(int, sys.stdin.readline().split())
    # Convert to zero-based index for string slicing
    l -= 1
    r -= 1
    # Print the result to stdout
    print(min_operations_to_beautiful(s, l, r))
